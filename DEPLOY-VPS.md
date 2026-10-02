# Deploy na VPS Hermes — 3 Minutos

## Opção 1: Automático (Recomendado)

```bash
# Do seu computador:
scp deploy-telegram-hermes.sh root@seu-vps-ip:/opt/

# Conectar na VPS:
ssh root@seu-vps-ip

# Rodar script (na VPS):
bash /opt/deploy-telegram-hermes.sh

# FIM! Vê os logs:
journalctl -u krakens-telegram -f
```

## Opção 2: Manual (Se quer mais controle)

```bash
# Na sua VPS:

# 1. Clone/update do repo
cd /opt
git clone https://github.com/emersonlourenco-droid/krakens-brain.git
cd krakens-brain

# 2. Instalar deps
pip install -r requirements-telegram.txt

# 3. Configurar .env
cp .env.example .env
nano .env
# Editar: TELEGRAM_TOKEN, HERMES_URL, etc (se necessário)

# 4. Testar (opcional)
python3 telegram-bridge.py
# Ctrl+C pra parar

# 5. Setup systemd
cp krakens-telegram.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable krakens-telegram
systemctl start krakens-telegram

# 6. Verificar
systemctl status krakens-telegram
journalctl -u krakens-telegram -f
```

## Descobrir IP da VPS

Se não sabe o IP:

```bash
# Do seu terminal local:
nslookup hermes-agent-qst4.srv2026911.hstgr.cloud
# Ou
ping hermes-agent-qst4.srv2026911.hstgr.cloud
```

## Testar No Telegram

Depois de deploy:

1. Abrir: https://t.me/Krakensaloudbot
2. Escrever: `/start`
3. Se der "Oi Emerson!", funcionou! 🎉

## Troubleshooting

### "Permission denied" no SSH
```bash
# Seus arquivos são muito restritivos. Abrir:
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
```

### Não consegue SSH
```bash
# Verificar SSH ativado:
ssh -v root@seu-vps-ip  # mostra detalhes

# Se não funcionar, pedir reset SSH pro host
```

### Serviço não inicia
```bash
# Ver logs detalhados:
journalctl -u krakens-telegram -n 50

# Reiniciar:
systemctl restart krakens-telegram

# Ver status:
systemctl status krakens-telegram
```

### Bot não responde no Telegram
1. Verificar serviço rodando: `systemctl status krakens-telegram`
2. Ver logs: `journalctl -u krakens-telegram -f`
3. Verificar HERMES_URL em `.env` está correto
4. Testar conexão: `curl https://hermes-agent-qst4.srv2026911.hstgr.cloud`

## Parar / Reiniciar

```bash
systemctl stop krakens-telegram       # parar
systemctl restart krakens-telegram    # reiniciar
systemctl disable krakens-telegram    # remover do boot
```

## Logs em Tempo Real

```bash
journalctl -u krakens-telegram -f

# Últimas 50 linhas:
journalctl -u krakens-telegram -n 50

# Só erros:
journalctl -u krakens-telegram | grep ERROR
```

---

**Pronto!** Seu DREDGE agora responde no Telegram 🚀

