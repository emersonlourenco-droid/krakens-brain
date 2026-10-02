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

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start"""
    await update.message.reply_text(
        "🤖 Oi! Sou DREDGE, agente quantitativo de Krakens.\n\n"
        "Pergunte o que quiser:\n"
        "• 'Como tá hoje?'\n"
        "• 'Performance da Beatriz?'\n"
        "• 'Tem alerta?'\n"
        "• 'Qual o ticket médio?'\n\n"
        "Eu trago dados brutos do dashboard. Sem alucinação. 📊"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Processa mensagem e chama DREDGE no Hermes"""
    user_message = update.message.text
    user_id = update.message.from_user.id
    
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
    Retorna resposta estruturada
    """
    try:
        # Endpoint Hermes (ajustar conforme API real)
        url = f"{HERMES_URL}/api/agent/dredge"
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {HERMES_API_KEY}" if HERMES_API_KEY else None
        }
        headers = {k: v for k, v in headers.items() if v}
        
        payload = {
            "message": prompt,
            "agent": "krakens-dredge",
            "format": "markdown"
        }
        
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        return data.get("response", "Sem resposta")
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro na chamada Hermes: {e}")
        return f"Não consegui conectar ao Hermes: {str(e)}"

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /help"""
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
    await update.message.chat.send_action("typing")
    response = call_dredge("Report de hoje: GBV, Meta%, Ticket, FTR, Ligações, Meetings")
    await update.message.reply_text(response, parse_mode="Markdown")

async def alerts_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /alerts - só vermelho"""
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
