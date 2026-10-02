#!/usr/bin/env python3
"""
Telegram Bridge para Krakens Brain DREDGE
Conecta @Krakensaloudbot (Telegram) ao Hermes DREDGE
"""

import os
import sys
import requests
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Config
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "8381631907:AAGcvif5OeTYPlaat6NJhCwuibhUkFhCzLI")
HERMES_URL = os.getenv("HERMES_URL", "https://hermes-agent-qst4.srv2026911.hstgr.cloud")
HERMES_API_KEY = os.getenv("HERMES_API_KEY", "")

# Segurança: apenas Emerson (8671621042)
ALLOWED_USER_ID = int(os.getenv("ALLOWED_USER_ID", "8671621042"))

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def is_authorized_user(user_id: int) -> bool:
    """Verifica se usuário está autorizado"""
    return user_id == ALLOWED_USER_ID

async def unauthorized(update: Update):
    """Rejeita usuário não autorizado"""
    logger.warning(f"❌ Acesso negado para user_id={update.message.from_user.id}")
    await update.message.reply_text(
        "🚫 Acesso negado.\n\n"
        f"Este bot é privado para Emerson (ID: {ALLOWED_USER_ID}).\n"
        "Se é você, atualize o ALLOWED_USER_ID."
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start"""
    if not is_authorized_user(update.message.from_user.id):
        await unauthorized(update)
        return

    await update.message.reply_text(
        "🤖 Oi Emerson! Sou DREDGE, agente quantitativo de Krakens.\n\n"
        "Pergunte o que quiser:\n"
        "• 'Como tá hoje?'\n"
        "• 'Performance da Beatriz?'\n"
        "• 'Tem alerta?'\n"
        "• 'Qual o ticket médio?'\n\n"
        "Eu trago dados brutos do dashboard. Sem alucinação. 📊"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Processa mensagem e chama DREDGE no Hermes"""
    user_id = update.message.from_user.id
    user_message = update.message.text

    # Filtro de segurança
    if not is_authorized_user(user_id):
        await unauthorized(update)
        return

    logger.info(f"[{user_id}] Mensagem: {user_message}")

    # Mostrar "typing"
    await update.message.chat.send_action("typing")
    
    try:
        # Chamar DREDGE via Hermes API
        response = call_dredge(user_message)
        
        if response:
            await update.message.reply_text(response, parse_mode="Markdown")
        else:
            await update.message.reply_text("⚠️ Não consegui buscar os dados. Tenta de novo?")
            
    except Exception as e:
        logger.error(f"Erro ao chamar DREDGE: {e}")
        await update.message.reply_text(f"❌ Erro: {str(e)}")

def call_dredge(prompt: str) -> str:
    """
    Chama @krakens-dredge no Hermes
    Tenta múltiplos endpoints até achar o correto
    """
    endpoints = [
        f"{HERMES_URL}/api/agent/dredge",
        f"{HERMES_URL}/agent/krakens-dredge",
        f"{HERMES_URL}/skills/krakens-dredge/run",
    ]

    headers = {
        "Content-Type": "application/json",
    }
    if HERMES_API_KEY:
        headers["Authorization"] = f"Bearer {HERMES_API_KEY}"

    payload = {
        "message": prompt,
        "agent": "krakens-dredge",
        "format": "markdown"
    }

    for url in endpoints:
        try:
            logger.info(f"Tentando endpoint: {url}")
            response = requests.post(url, json=payload, headers=headers, timeout=15)

            if response.status_code == 200:
                data = response.json()
                result = data.get("response") or data.get("data") or str(data)
                logger.info(f"✅ Sucesso em {url}")
                return result
            elif response.status_code == 404:
                logger.debug(f"404 em {url}, tentando próximo...")
                continue
            else:
                logger.warning(f"Status {response.status_code} em {url}")

        except requests.exceptions.Timeout:
            logger.warning(f"Timeout em {url}")
            continue
        except requests.exceptions.RequestException as e:
            logger.warning(f"Erro em {url}: {str(e)}")
            continue

    logger.error(f"Nenhum endpoint funcionou para: {prompt}")
    return "⚠️ Não consegui conectar ao Hermes. Verifica a configuração HERMES_URL?"

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /help"""
    if not is_authorized_user(update.message.from_user.id):
        await unauthorized(update)
        return

    await update.message.reply_text(
        "📖 **DREDGE Commands**\n\n"
        "/start - Iniciar\n"
        "/help - Este menu\n"
        "/status - Status do dashboard\n"
        "/alerts - Verificar alertas críticos\n\n"
        "Ou só escreva naturalmente: 'performance de hoje?'"
    )

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /status - report rápido"""
    if not is_authorized_user(update.message.from_user.id):
        await unauthorized(update)
        return

    await update.message.chat.send_action("typing")
    response = call_dredge("Report de hoje: GBV, Meta%, Ticket, FTR, Ligações, Meetings")
    await update.message.reply_text(response, parse_mode="Markdown")

async def alerts_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /alerts - só vermelho"""
    if not is_authorized_user(update.message.from_user.id):
        await unauthorized(update)
        return

    await update.message.chat.send_action("typing")
    response = call_dredge("Que alertas temos agora? Só o vermelho.")
    await update.message.reply_text(response, parse_mode="Markdown")

def main():
    """Inicia o bot"""
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("status", status_command))
    app.add_handler(CommandHandler("alerts", alerts_command))
    
    # Mensagens normais
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    logger.info("🚀 DREDGE Telegram Bridge iniciado")
    logger.info(f"Bot: @Krakensaloudbot")
    logger.info(f"Hermes: {HERMES_URL}")
    
    app.run_polling()

if __name__ == "__main__":
    main()
