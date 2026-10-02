# Dashboard Setup

DREDGE está configurado para acessar:
1. **Primary**: Google Data Studio (requer login)
2. **Fallback**: `/tmp/krakens-brain/metricas/dashboard.json` (442KB)

## Pra ativar o fallback no Hermes:

Copie o arquivo dashboard.json pra um caminho acessível:
```bash
cp /tmp/krakens-brain/metricas/dashboard.json /path/to/hermes/data/dashboard.json
```

Ou configure a variável de ambiente:
```bash
export DREDGE_DASHBOARD_PATH=/tmp/krakens-brain/metricas/dashboard.json
```

Dashboard.json contém:
- KPIs completos (GBV, Meta%, Ticket, FTR, etc)
- Performance por vendedor
- Histórico do funil
- Alertas e status

**Status**: Pronto pra consulta, fallback testado ✅
