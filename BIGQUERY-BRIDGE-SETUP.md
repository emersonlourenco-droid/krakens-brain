# BigQuery Bridge — Setup

Script que roda no seu PC e expõe BigQuery como API HTTP pra Hermes acessar.

---

## Quick Start

### Passo 1: Instalar dependências (no seu PC)

```bash
pip install -r requirements-bigquery.txt
```

### Passo 2: Autenticar com Google Cloud

```bash
gcloud auth application-default login
```

Vai abrir navegador pra você fazer login. Depois é automático.

### Passo 3: Rodar o bridge

```bash
python bigquery-bridge.py
```

Ou com Gunicorn (produção):

```bash
gunicorn -w 4 -b 0.0.0.0:5000 bigquery-bridge:app
```

### Passo 4: Testar

```bash
curl http://localhost:5000/health
curl http://localhost:5000/krakens/hoje
curl http://localhost:5000/krakens/funil
curl http://localhost:5000/krakens/vendedor/Beatriz
curl http://localhost:5000/krakens/conversas?limit=20
```

---

## Endpoints Disponíveis

### `/health`
Status do bridge

```bash
GET http://localhost:5000/health
```

Resposta:
```json
{
  "status": "ok",
  "timestamp": "2026-10-02T14:30:00",
  "project": "aloud-rox",
  "dataset": "alouddatamarket"
}
```

### `/krakens/hoje`
Relatório do time de hoje

```bash
GET http://localhost:5000/krakens/hoje
```

Retorna por vendedor:
- leads (quantidade)
- gbv (total)
- ticket_medio
- ftr_minutos
- ligacoes
- meetings
- fechamentos
- taxa_conversao_pct

### `/krakens/funil`
Distribuição do funil

```bash
GET http://localhost:5000/krakens/funil
```

Retorna:
- etapa (S1, S2, S3, ...)
- quantidade
- percentual

### `/krakens/vendedor/<name>`
Performance de 1 vendedor (últimos 7 dias)

```bash
GET http://localhost:5000/krakens/vendedor/Beatriz
```

### `/krakens/conversas`
Últimas conversas (pra SCOPE CODEX analisar)

```bash
GET http://localhost:5000/krakens/conversas?limit=20
```

---

## Configuração Avançada

### Variáveis de Ambiente

```bash
# .env
BRIDGE_PORT=5000                          # Porta padrão
GCP_PROJECT_ID=aloud-rox                  # Seu projeto
GCP_DATASET_ID=alouddatamarket            # Seu dataset
GOOGLE_APPLICATION_CREDENTIALS=/path/key  # Se usar service account
```

### Rodar 24/7 (Mac/Linux)

#### Opção 1: Systemd (Linux)

```ini
# /etc/systemd/system/bigquery-bridge.service
[Unit]
Description=BigQuery Bridge for Krakens Hermes
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=/path/to/krakens-brain
ExecStart=/usr/bin/python3 /path/to/bigquery-bridge.py
Restart=on-failure
RestartSec=10

Environment="BRIDGE_PORT=5000"
Environment="GCP_PROJECT_ID=aloud-rox"
Environment="GCP_DATASET_ID=alouddatamarket"

[Install]
WantedBy=multi-user.target
```

Start:
```bash
sudo systemctl enable bigquery-bridge.service
sudo systemctl start bigquery-bridge.service
sudo systemctl status bigquery-bridge.service
```

#### Opção 2: LaunchAgent (Mac)

```xml
<!-- ~/Library/LaunchAgents/com.krakens.bigquery-bridge.plist -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.krakens.bigquery-bridge</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/python3</string>
        <string>/path/to/bigquery-bridge.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/var/log/bigquery-bridge.log</string>
    <key>StandardErrorPath</key>
    <string>/var/log/bigquery-bridge.err</string>
</dict>
</plist>
```

Load:
```bash
launchctl load ~/Library/LaunchAgents/com.krakens.bigquery-bridge.plist
launchctl start com.krakens.bigquery-bridge
launchctl list | grep bigquery
```

---

## Integração com Hermes

Depois que o bridge estiver rodando:

1. Configure Hermes pra acessar `http://seu-pc-ip:5000`
2. DREDGE faz queries via bridge
3. Dados em tempo real no relatório

```yaml
# hermes-config.json
data_sources:
  bigquery:
    url: "http://192.168.x.x:5000"  # IP do seu PC
    endpoints:
      hoje: "/krakens/hoje"
      funil: "/krakens/funil"
      conversas: "/krakens/conversas"
```

---

## Troubleshooting

**"Connection refused"**
- Bridge não está rodando?
- `python bigquery-bridge.py` no seu PC

**"401 Unauthorized"**
- Google Cloud auth expirou
- `gcloud auth application-default login` de novo

**"Table not found"**
- Tabelas não existem no dataset
- Atualize queries no script com nomes reais

---

## Próximas Etapas

1. ✅ Rodar bridge no PC
2. ✅ Testar endpoints com curl
3. ✅ Conectar Hermes
4. ✅ DREDGE passa a puxar dados em tempo real
5. ✅ SCOPE CODEX analisa conversas

