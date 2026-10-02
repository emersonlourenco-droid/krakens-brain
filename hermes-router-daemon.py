#!/usr/bin/env python3
"""
Hermes Router Daemon — Roteamento Automático MAESTRO
Monitora mensagens do Hermes e roteia automaticamente pra @maestro-relatorio
quando detecta palavras-chave sobre time/performance.
"""

import os
import time
import logging
from datetime import datetime
import requests
from typing import List

# Config
HERMES_URL = os.getenv("HERMES_URL", "https://hermes-agent-qst4.srv2026911.hstgr.cloud")
HERMES_API_KEY = os.getenv("HERMES_API_KEY", "")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "30"))  # segundos

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Palavras-chave que ativam roteamento
ROUTING_KEYWORDS = [
    "time", "status", "performance", "funil", "meta", 
    "conversão", "ligações", "leads", "ticket", "alertas",
    "vendedor", "beatriz", "joão", "jesiel", "tiago", "ana", "fabiano", "emerson"
]

def contains_routing_keyword(text: str) -> bool:
    """Verifica se texto contém palavras-chave de routing"""
    text_lower = text.lower()
    for keyword in ROUTING_KEYWORDS:
        if keyword in text_lower:
            return True
    return False

def route_message(original_message: str) -> str:
    """Roteia mensagem pra @maestro-relatorio"""
    # Adiciona @maestro-relatorio no início se não estiver lá
    if "@maestro-relatorio" not in original_message:
        return f"@maestro-relatorio {original_message}"
    return original_message

def send_to_hermes(routed_message: str) -> bool:
    """Envia mensagem roteiada pra Hermes"""
    endpoints = [
        f"{HERMES_URL}/api/chat",
        f"{HERMES_URL}/chat/send",
        f"{HERMES_URL}/api/message",
    ]

    headers = {
        "Content-Type": "application/json",
    }
    if HERMES_API_KEY:
        headers["Authorization"] = f"Bearer {HERMES_API_KEY}"

    payload = {
        "message": routed_message,
        "route": "maestro-relatorio"
    }

    for url in endpoints:
        try:
            logger.info(f"Tentando enviar pra {url}: {routed_message[:50]}...")
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            
            if response.status_code in [200, 201, 202]:
                logger.info(f"✅ Roteado com sucesso: {routed_message[:50]}...")
                return True
                
        except requests.exceptions.RequestException as e:
            logger.warning(f"Erro em {url}: {str(e)}")
            continue

    logger.error(f"Falhou ao rotear: {routed_message[:50]}...")
    return False

def monitor_hermes():
    """Loop principal — monitora Hermes e roteia mensagens"""
    logger.info("🚀 Hermes Router Daemon iniciado")
    logger.info(f"Hermes URL: {HERMES_URL}")
    logger.info(f"Check interval: {CHECK_INTERVAL}s")
    logger.info(f"Palavras-chave: {', '.join(ROUTING_KEYWORDS)}")
    
    last_check = datetime.now()
    
    while True:
        try:
            # Fetch mensagens recentes do Hermes
            response = requests.get(
                f"{HERMES_URL}/api/sessions?limit=10",
                headers={"Authorization": f"Bearer {HERMES_API_KEY}"} if HERMES_API_KEY else {},
                timeout=10
            )
            
            if response.status_code == 200:
                sessions = response.json()
                
                # Processa cada sessão
                for session in sessions.get("sessions", []):
                    messages = session.get("messages", [])
                    
                    for msg in messages:
                        # Verifica se precisa rotear
                        content = msg.get("content", "")
                        if content and contains_routing_keyword(content):
                            routed = route_message(content)
                            if routed != content:  # Só envia se foi modificado
                                send_to_hermes(routed)
                                
        except requests.exceptions.RequestException as e:
            logger.warning(f"Erro ao conectar Hermes: {str(e)}")
        except Exception as e:
            logger.error(f"Erro desconhecido: {str(e)}")
        
        # Wait until next check
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    try:
        monitor_hermes()
    except KeyboardInterrupt:
        logger.info("🛑 Router daemon interrompido")
