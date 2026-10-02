# Roteamento Automático — MAESTRO Router

**Status**: ✅ Pronto pra usar

## O que é

Automático: qualquer pergunta sobre time/performance → automaticamente roteia pra @maestro-relatorio

## Como funciona

```
"Como tá o time?" 
→ Sistema detecta "time"
→ Roteia pra @maestro-relatorio
→ MAESTRO responde com relatório
```

## 3 Formas de Ativar

### 1️⃣ **Daemon Python** (Produção — Recomendado)

Cria um background worker que monitora Hermes 24/7.

```bash
# No seu VPS:
python3 hermes-router-daemon.py &

# Ou com systemd (pra auto-restart):
sudo cp hermes-router-daemon.py /opt/hermes/router
sudo cp hermes-router-daemon.service /etc/systemd/system/
sudo systemctl enable hermes-router-daemon.service
sudo systemctl start hermes-router-daemon.service
```

Variáveis de ambiente:
```bash
export HERMES_URL="https://hermes-agent-qst4.srv2026911.hstgr.cloud"
export HERMES_API_KEY="seu-api-key-aqui"
export CHECK_INTERVAL="30"  # segundos entre checks
```

### 2️⃣ **Maestro Router Skill** (Manual)

Use quando quiser: `/maestro-router <pergunta>`

```
User: "/maestro-router Como tá o time?"
System: Roteia pra @maestro-relatorio
MAESTRO: Retorna relatório
```

Já disponível em `/skills/maestro-router/SKILL.md`

### 3️⃣ **Manual** (sempre funciona)

Basta digitar `@maestro-relatorio` + pergunta:

```
User: "@maestro-relatorio Como tá o time?"
MAESTRO: Relatório
```

## Palavras-chave que Ativam

Detectadas automaticamente:

- **Métricas**: time, status, performance, meta, conversão, ticket, leads, ligações, alertas, funil
- **Vendedores**: Beatriz, João, Jesiel, Tiago, Ana, Fabiano, Emerson

## Instalação (Daemon)

### Passo 1: Arquivo de Serviço

```bash
# Crie: hermes-router-daemon.service
```

```ini
[Unit]
Description=Hermes Router Daemon — Roteamento Automático
After=network.target

[Service]
Type=simple
User=hermes
WorkingDirectory=/opt/hermes
ExecStart=/usr/bin/python3 /opt/hermes/router/hermes-router-daemon.py
Restart=on-failure
RestartSec=10
Environment="HERMES_URL=https://hermes-agent-qst4.srv2026911.hstgr.cloud"
Environment="HERMES_API_KEY=seu-api-key"

[Install]
WantedBy=multi-user.target
```

### Passo 2: Install & Start

```bash
sudo cp hermes-router-daemon.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable hermes-router-daemon.service
sudo systemctl start hermes-router-daemon.service

# Verificar status:
sudo systemctl status hermes-router-daemon.service

# Ver logs:
sudo journalctl -u hermes-router-daemon.service -f
```

## Logs

Monitore o daemon:

```bash
tail -f /var/log/hermes-router.log
```

Ou com systemd:

```bash
journalctl -u hermes-router-daemon.service -f
```

## Parar o Daemon

```bash
sudo systemctl stop hermes-router-daemon.service
```

## Troubleshooting

**"Conexão recusada"**
- Verifica HERMES_URL
- Verifica se Hermes está rodando

**"401 Unauthorized"**
- Verifica HERMES_API_KEY
- Regenera key em Hermes → CONFIG → KEYS

**"Nenhuma mensagem roteiada"**
- Verifica logs: `journalctl -u hermes-router-daemon.service -f`
- Confirma que palavras-chave estão corretas
- Testa com `/maestro-router "Como tá o time?"`

---

**Próximos passos**: 
- Escolha a forma (Daemon / Manual)
- Vá em CHAT e teste
- Pergunte sobre seu time sem @ — sistema roteia sozinho

