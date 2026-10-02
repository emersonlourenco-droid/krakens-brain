#!/bin/bash
# Deploy Telegram Bridge no Hermes VPS
# Rode como: bash deploy-telegram-hermes.sh

set -e

echo "🚀 Iniciando deploy Telegram Bridge..."

# Detectar usuário/permissões
if [ "$EUID" -ne 0 ]; then 
   echo "❌ Execute como root: sudo bash deploy-telegram-hermes.sh"
   exit 1
fi

INSTALL_DIR="/opt/krakens-brain"

echo "📁 Criando/atualizando $INSTALL_DIR..."
mkdir -p $INSTALL_DIR
cd $INSTALL_DIR

echo "📥 Puxando código do GitHub..."
if [ -d ".git" ]; then
    git pull origin main
else
    git clone https://github.com/emersonlourenco-droid/krakens-brain.git .
fi

echo "📦 Instalando dependências Python..."
pip install -r requirements-telegram.txt

echo "📝 Configurando .env..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "✅ .env criado. Editá-lo depois se necessário."
else
    echo "⚠️ .env já existe. Pulando (se precisa mudar, editar manualmente)"
fi

echo "🔧 Instalando systemd service..."
cp krakens-telegram.service /etc/systemd/system/
systemctl daemon-reload

echo "🟢 Habilitando serviço..."
systemctl enable krakens-telegram

echo "▶️ Iniciando krakens-telegram..."
systemctl start krakens-telegram

echo "✅ Deploy completo!"
echo ""
echo "📊 Status:"
systemctl status krakens-telegram

echo ""
echo "📋 Próximos passos:"
echo "1. Editar /opt/krakens-brain/.env se necessário"
echo "2. Testar no Telegram: https://t.me/Krakensaloudbot"
echo "3. Ver logs: journalctl -u krakens-telegram -f"
echo ""
echo "🎯 Tudo pronto!"

