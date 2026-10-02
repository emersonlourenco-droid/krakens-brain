# DREDGE — Configuração de Fonte de Dados

DREDGE precisa puxar dados de uma fonte que ele consegue acessar.

**Google Data Studio** ❌ — Requer login web (não funciona)  
**BigQuery Bridge** ✅ — HTTP API local (perfeito)

---

## Instruções Atualizadas para DREDGE

### Ao receber pergunta sobre números:

```
1. Entender a pergunta
2. Preparar query inteligente
3. Acessar http://localhost:5000 (BigQuery Bridge)
4. Chamar endpoint apropriado:
   - /krakens/hoje → "Como tá hoje?"
   - /krakens/funil → "Qual é o funil?"
   - /krakens/vendedor/<nome> → "Como tá [vendedor]?"
   - /krakens/conversas → "Últimas conversas"
5. Estruturar resposta (tabela + alertas + insights)
6. Enviar via Telegram
```

### Endpoints do Bridge

```
GET http://localhost:5000/health
  → Verifica se bridge está rodando

GET http://localhost:5000/krakens/hoje
  → GBV, meta, ticket, FTR, ligações, conversão por vendedor

GET http://localhost:5000/krakels/funil
  → Distribuição S1-S9

GET http://localhost:5000/krakens/vendedor/Beatriz
  → Performance individual

GET http://localhost:5000/krakens/conversas?limit=20
  → Últimas conversas (SCOPE CODEX usa)
```

---

## Se Bridge Não Estiver Rodando

DREDGE deve retornar:

```
"Opa, não consegui puxar os dados porque o BigQuery Bridge não está rodando no seu PC.

Você precisa:
1. Abrir terminal
2. Rodar: python bigquery-bridge.py
3. Deixar rodando
4. Tentar de novo

Precisa de ajuda?"
```

Nunca retorna erro criptográfico. Sempre claro.

---

## Na Prática

**Pergunta via Telegram**:
```
"Como tá o time?"
```

**DREDGE faz**:
```python
# 1. Detecta que é pergunta sobre time
# 2. Faz request GET http://localhost:5000/krakens/hoje
# 3. Recebe JSON com dados de hoje
# 4. Estrutura em tabela
# 5. Adiciona alertas
# 6. Envia resposta no Telegram
```

**Resposta**:
```
## 📊 Relatório Krakens — Hoje

| Vendedor | GBV | Meta% | Ticket | FTR |
|----------|-----|-------|--------|-----|
| Beatriz | R$45k | 120% | R$3.2k | 11min |
| João | R$38k | 95% | R$3.1k | 16min |

🔴 Alertas:
- João: 95% meta (abaixo de 100%)

📈 Gargalo:
- 70% em abertura (FTR alto)
```

---

## Checklist de Setup

- [ ] BigQuery Bridge instalado no PC
- [ ] Bridge rodando (`python bigquery-bridge.py`)
- [ ] Bridge acessível em `http://localhost:5000`
- [ ] DREDGE testa `/health` primeiro
- [ ] Se falhar, avisa ao usuário
- [ ] Se funcionar, puxa dados estruturados

