# Telegram + DREDGE + Hermes 🚀

Você agora pode falar com DREDGE direto do Telegram.

## O Que é

- **Bot**: @Krakensaloudbot
- **Token**: Já criado (vê em TELEGRAM-SETUP.md)
- **Bridge**: Python script que conecta Telegram → Hermes → DREDGE
- **Deploy**: Systemd service na sua VPS

## Quick Start

### Na sua VPS (3 passos)

```bash
# 1. Git pull das mudanças
cd /opt/krakens-brain
git pull origin main

# 2. Instalar dependências
pip install -r requirements-telegram.txt

# 3. Rodar bridge (teste rápido)
python3 telegram-bridge.py
```

Se ver "🚀 DREDGE Telegram Bridge iniciado", tá funcionando!

### Setup Permanente (systemd)

```bash
# 1. Configurar .env
cp .env.example .env
nano .env  # editar HERMES_URL, etc

# 2. Instalar service
cp krakens-telegram.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable krakens-telegram
systemctl start krakens-telegram

# 3. Testar
systemctl status krakens-telegram
```

### No Telegram

1. Abrir: https://t.me/Krakensaloudbot
2. Escrever qualquer pergunta:
   - "Como tá hoje?"
   - "Performance da Beatriz?"
   - "Tem alerta?"
   - "Qual o ticket médio?"

DREDGE responde com dados brutos do dashboard. Sem alucinação. 📊

## Comandos

| Comando | O que faz |
|---------|-----------|
| `/start` | Iniciar, ver instruções |
| `/status` | Report rápido de hoje |
| `/alerts` | Alertas críticos (só vermelho) |
| `/help` | Este menu |
| Mensagem normal | Qualquer pergunta |

## Arquitetura

```
Telegram @Krakensaloudbot
    ↓
telegram-bridge.py (VPS)
    ↓
Hermes API
    ↓
DREDGE (agente @krakens-dredge)
    ↓
Google Data Studio
    ↓
Resposta em Markdown
    ↓
Telegram (volta pra você)
```

## Variáveis Importantes

Editar em `.env`:

```bash
# Seu bot (já preenchido)
TELEGRAM_TOKEN=8381631907:AAGcvif5OeTYPlaat6NJhCwuibhUkFhCzLI

# URL da sua VPS Hermes
HERMES_URL=https://hermes-agent-qst4.srv2026911.hstgr.cloud

# API Key Hermes (deixar em branco por enquanto)
HERMES_API_KEY=
```

## Logs em Tempo Real

```bash
journalctl -u krakens-telegram -f
```

## Parar / Reiniciar

```bash
systemctl stop krakens-telegram      # parar
systemctl restart krakens-telegram   # reiniciar
```

## Detalhes Técnicos

Ver: `TELEGRAM-SETUP.md` (instruções completas + troubleshooting)

---

Bot criado em 2026-10-02 | DREDGE ready 🎯

