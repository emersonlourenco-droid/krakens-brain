# Setup Telegram Bridge na VPS Hermes

## 1. Copiar arquivos pra VPS

```bash
scp -r telegram-bridge.py requirements-telegram.txt .env.example krakens-telegram.service root@seu-vps:/opt/krakens-brain/
```

## 2. Conectar na VPS

```bash
ssh root@seu-vps
cd /opt/krakens-brain
```

## 3. Instalar dependências

```bash
pip install -r requirements-telegram.txt
```

## 4. Configurar variáveis (.env)

```bash
cp .env.example .env
nano .env
```

Editar:
- `TELEGRAM_TOKEN=` (já tem, é o token do bot)
- `HERMES_URL=` (sua URL Hermes)
- `HERMES_API_KEY=` (deixar em branco por enquanto, vamos gerar)

Salvar: CTRL+O → Enter → CTRL+X

## 5. Testar conexão

```bash
python3 telegram-bridge.py
```

Se aparecer "🚀 DREDGE Telegram Bridge iniciado", funcionou! CTRL+C pra parar.

## 6. Instalar como serviço systemd

```bash
cp krakens-telegram.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable krakens-telegram
systemctl start krakens-telegram
```

## 7. Verificar status

```bash
systemctl status krakens-telegram
journalctl -u krakens-telegram -f  # logs em tempo real
```

## 8. Testar no Telegram

Abra: https://t.me/Krakensaloudbot

Escreva: `Como tá hoje?`

Deve retornar os dados do dashboard!

## Troubleshooting

### "Falha ao conectar ao Hermes"
- Verificar HERMES_URL em .env
- Verificar se Hermes está rodando: `curl https://hermes-agent-qst4.srv2026911.hstgr.cloud`

### "ImportError: No module named telegram"
```bash
pip install --upgrade python-telegram-bot
```

### Logs não aparecem
```bash
journalctl -u krakens-telegram --no-pager
```

## Parar/Reiniciar

```bash
systemctl stop krakens-telegram     # parar
systemctl restart krakens-telegram  # reiniciar
systemctl disable krakens-telegram  # remover do boot
```

