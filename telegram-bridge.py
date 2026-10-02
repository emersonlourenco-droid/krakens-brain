#!/usr/bin/env python3
"""
Telegram Bridge para Krakens Brain DREDGE
Conecta @Krakensaloudbot ao Hermes DREDGE via BigQuery Bridge
"""

import os
import sys
import requests
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Config
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "8381631907:AAGcvif5OeTYPlaat6NJhCwuibhUkFhCzLI")
BIGQUERY_BRIDGE = os.getenv("BIGQUERY_BRIDGE", "http://localhost:5000")

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
        "🤖 Oi Emerson! Sou o bot de dados do Krakens.\n\n"
        "Pergunte sobre números:\n"
        "• 'Como tá o time?'\n"
        "• 'Performance da Beatriz?'\n"
        "• 'Tem alerta?'\n"
        "• 'Qual é o funil?'\n\n"
        "Só números por enquanto (qualitativo vem depois). 📊"
    )

def is_numbers_question(text: str) -> bool:
    """Detecta se pergunta é sobre números"""
    keywords = [
        'time', 'performance', 'meta', 'quanto', 'qual',
        'hoje', 'semana', 'mês', 'gbv', 'ticket', 'ftr',
        'ligações', 'meetings', 'conversão', 'funil', 'alerta',
        'vendedor', 'beatriz', 'joão', 'tiago', 'ana', 'jesiel',
        'gargalo', 'leads', 'fechamento'
    ]
    return any(kw in text.lower() for kw in keywords)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Processa mensagem e chama DREDGE no BigQuery Bridge"""
    user_id = update.message.from_user.id
    user_message = update.message.text

    # Filtro de segurança
    if not is_authorized_user(user_id):
        await unauthorized(update)
        return

    logger.info(f"[{user_id}] Mensagem: {user_message}")

    # Detecta se é pergunta sobre números
    if not is_numbers_question(user_message):
        await update.message.reply_text(
            "Posso trazer dados numéricos do time.\n\n"
            "Tenta perguntar: 'Como tá o time?', 'Performance da Beatriz?', etc"
        )
        return

    # Mostrar "typing"
    await update.message.chat.send_action("typing")

    try:
        # Chamar DREDGE via BigQuery Bridge
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
    Chama DREDGE via BigQuery Bridge
    Endpoints:
    - /krakens/hoje
    - /krakens/funil
    - /krakens/vendedor/<nome>
    - /krakens/conversas
    """
    headers = {"Content-Type": "application/json"}

    # Detectar qual endpoint usar
    endpoint = detect_endpoint(prompt)

    if not endpoint:
        return "❌ Não consegui entender sua pergunta. Tenta: 'Como tá o time?'"

    url = f"{BIGQUERY_BRIDGE}{endpoint}"

    try:
        logger.info(f"Chamando: {url}")
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()
            formatted = format_response(data, endpoint)
            logger.info(f"✅ Sucesso: {endpoint}")
            return formatted

        elif response.status_code == 404:
            logger.error(f"❌ Bridge não encontrou dados em {endpoint}")
            return "⚠️ Bridge não encontrou os dados. Tá rodando? `python bigquery-bridge.py`"

        else:
            logger.error(f"❌ Status {response.status_code}")
            return f"⚠️ Erro ao puxar dados (status {response.status_code})"

    except requests.exceptions.ConnectionError:
        logger.error("❌ Não consegui conectar ao BigQuery Bridge")
        return (
            "🔴 **BigQuery Bridge não está rodando!**\n\n"
            "Você precisa rodar no seu PC:\n"
            "`python bigquery-bridge.py`\n\n"
            "Deixa rodando e tenta de novo."
        )

    except requests.exceptions.Timeout:
        logger.error("❌ Timeout ao chamar bridge")
        return "⚠️ Timeout. Bridge tá muito lento ou não respondeu."

    except Exception as e:
        logger.error(f"❌ Erro: {str(e)}")
        return f"❌ Erro inesperado: {str(e)}"

def detect_endpoint(prompt: str) -> str:
    """Detecta qual endpoint chamar baseado na pergunta"""
    prompt_lower = prompt.lower()

    # Vendedor específico
    vendedores = ['beatriz', 'joão', 'tiago', 'ana', 'jesiel', 'fabiano']
    for vendedor in vendedores:
        if vendedor in prompt_lower:
            return f"/krakens/vendedor/{vendedor.capitalize()}"

    # Funil
    if any(word in prompt_lower for word in ['funil', 'etapa', 'acúmulo', 'onde tá parado']):
        return "/krakens/funil"

    # Conversas (qualitativo - futuro)
    if any(word in prompt_lower for word in ['conversa', 'áudio', 'qualitativo']):
        return "/krakens/conversas"

    # Padrão: hoje
    return "/krakens/hoje"

def format_response(data: dict, endpoint: str) -> str:
    """Formata resposta JSON em Markdown legível"""
    try:
        if endpoint == "/krakens/hoje":
            return format_hoje(data)
        elif endpoint == "/krakens/funil":
            return format_funil(data)
        elif "/vendedor/" in endpoint:
            return format_vendedor(data)
        elif endpoint == "/krakens/conversas":
            return format_conversas(data)
        else:
            return f"📊 Dados:\n```json\n{str(data)}\n```"
    except Exception as e:
        logger.error(f"Erro ao formatar: {e}")
        return f"Dados brutos:\n{str(data)}"

def format_hoje(data: dict) -> str:
    """Formata resposta de /krakens/hoje"""
    timestamp = data.get('timestamp', 'hoje')
    total_gbv = data.get('total_gbv', 0)
    items = data.get('data', [])

    if not items:
        return "❌ Sem dados para hoje"

    header = f"## 📊 Relatório Krakens — {timestamp}\n\n"
    header += f"**GBV Total: R$ {total_gbv:,.0f}**\n\n"

    # Tabela
    table = "| Vendedor | GBV | Meta% | Ticket | FTR | Status |\n"
    table += "|----------|-----|-------|--------|-----|--------|\n"

    for item in items:
        vendedor = item.get('vendedor', '?')
        gbv = item.get('gbv', 0)
        meta_pct = item.get('taxa_conversao_pct', 0)  # Usar conversão como proxy se meta não tiver
        ticket = item.get('ticket_medio', 0)
        ftr = item.get('ftr_minutos', 0)

        # Status baseado em meta
        if meta_pct >= 100:
            status = "🟢"
        elif meta_pct >= 65:
            status = "🟠"
        else:
            status = "🔴"

        table += f"| {vendedor} | R${gbv:,.0f} | {meta_pct:.0f}% | R${ticket:,.0f} | {ftr:.0f}m | {status} |\n"

    return header + table

def format_funil(data: dict) -> str:
    """Formata resposta de /krakens/funil"""
    items = data.get('data', [])

    if not items:
        return "❌ Sem dados de funil"

    header = "## 📈 Funil do Krakens\n\n"
    header += "| Etapa | Quantidade | % |\n"
    header += "|-------|------------|---|\n"

    for item in items:
        etapa = item.get('etapa', '?')
        qtd = item.get('quantidade', 0)
        pct = item.get('percentual', 0)

        header += f"| {etapa} | {qtd} | {pct:.1f}% |\n"

    return header

def format_vendedor(data: dict) -> str:
    """Formata resposta de /krakens/vendedor/<nome>"""
    vendedor = data.get('vendedor', '?')
    leads = data.get('leads_7dias', 0)
    gbv = data.get('gbv_7dias', 0)
    ticket = data.get('ticket_medio', 0)
    ftr = data.get('ftr_minutos', 0)
    ligacoes = data.get('ligacoes', 0)
    fechamentos = data.get('fechamentos', 0)

    return (
        f"## 📊 {vendedor}\n\n"
        f"**Últimos 7 dias:**\n"
        f"- Leads: {leads}\n"
        f"- GBV: R$ {gbv:,.0f}\n"
        f"- Ticket Médio: R$ {ticket:,.0f}\n"
        f"- FTR: {ftr:.0f} min\n"
        f"- Ligações: {ligacoes}\n"
        f"- Fechamentos: {fechamentos}\n"
    )

def format_conversas(data: dict) -> str:
    """Formata resposta de /krakens/conversas"""
    items = data.get('data', [])

    if not items:
        return "❌ Sem conversas registradas"

    header = "## 💬 Últimas Conversas\n\n"

    for i, item in enumerate(items[:5], 1):  # Top 5
        vendedor = item.get('vendedor', '?')
        tipo = item.get('tipo', '?')
        duracao = item.get('duracao_audio_seg', 0)

        header += f"{i}. **{vendedor}** ({tipo})\n"
        if duracao > 0:
            header += f"   Duração: {duracao}s\n"

    return header

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /help"""
    if not is_authorized_user(update.message.from_user.id):
        await unauthorized(update)
        return

    await update.message.reply_text(
        "📖 **Bot Krakens**\n\n"
        "/start - Iniciar\n"
        "/help - Este menu\n\n"
        "**Pergunte sobre:**\n"
        "• Como tá o time?\n"
        "• Performance da Beatriz?\n"
        "• Qual é o funil?\n"
        "• Tem alerta?"
    )

def main():
    """Inicia o bot"""
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Mensagens normais
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("🚀 Krakens Telegram Bridge iniciado")
    logger.info(f"Bot: @Krakensaloudbot")
    logger.info(f"BigQuery Bridge: {BIGQUERY_BRIDGE}")

    app.run_polling()

if __name__ == "__main__":
    main()

