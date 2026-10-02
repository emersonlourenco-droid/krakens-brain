# DREDGE — Usar BigQuery Bridge

DREDGE não deve mais tentar:
- ❌ Google Data Studio (pede login)
- ❌ Arquivo JSON local (não existe no Hermes)

DREDGE DEVE usar:
- ✅ **BigQuery Bridge via HTTP** (http://seu-pc-ip:5000)

---

## Instruções para DREDGE

Quando solicitado relatório sobre números do time:

### 1. Verificar se Bridge está rodando

```
GET http://seu-pc-ip:5000/health
```

Se responder `{"status": "ok"}` → bridge está rodando ✅

Se der erro de conexão → "BigQuery Bridge não está rodando. Você precisa: `python bigquery-bridge.py` no seu PC"

### 2. Chamar endpoint apropriado

**Para "Como tá o time?":**
```
GET http://seu-pc-ip:5000/krakens/hoje
```

Retorna:
```json
{
  "timestamp": "2026-10-02T14:30:00",
  "data": [
    {
      "vendedor": "Beatriz",
      "leads": 26,
      "gbv": 45000,
      "ticket_medio": 3200,
      "ftr_minutos": 11,
      "ligacoes": 12,
      "meetings": 2,
      "fechamentos": 3,
      "taxa_conversao_pct": 85
    }
  ],
  "total_gbv": 264000
}
```

**Para "Qual é o funil?":**
```
GET http://seu-pc-ip:5000/krakens/funil
```

**Para "Performance da Beatriz?":**
```
GET http://seu-pc-ip:5000/krakens/vendedor/Beatriz
```

### 3. Estruturar resposta

Recebe JSON → estrutura em tabela Markdown → retorna

Exemplo:

```markdown
## 📊 Relatório Krakens — Hoje

| Vendedor | GBV | Meta% | Ticket | FTR | Status |
|----------|-----|-------|--------|-----|--------|
| Beatriz | R$45k | 125% | R$3.2k | 11min | 🟢 |
| João | R$38k | 95% | R$3.1k | 16min | 🟠 |

### 🔴 Alertas
- João: 95% meta (abaixo de 100%)

### 📈 Gargalo
- 70% em abertura (S1-S3)
```

---

## Como Configurar no Hermes

### Opção 1: Atualizar Prompt de DREDGE

No SOUL-DREDGE-AVANCADO.md, section "Regra #4: Dados Que Você Tem Acesso", mudar:

```
Via BigQuery Bridge (http://localhost:5000):
```

Para:

```
Via BigQuery Bridge (http://seu-pc-ip:5000):
```

### Opção 2: Skill que Chama Bridge

Criar skill que faz a chamada HTTP:

```
maestro-relatorio/call-bigquery-bridge.md
```

Com instruções de como chamar e estruturar.

---

## Erro Handling

Se bridge falhar:

```python
try:
    response = requests.get(f"{BRIDGE_URL}{endpoint}")
    if response.status_code == 200:
        return format_as_markdown(response.json())
    else:
        return "⚠️ Bridge retornou erro. Status: " + str(response.status_code)
except ConnectionError:
    return "🔴 BigQuery Bridge não está rodando.\nRode no seu PC: python bigquery-bridge.py"
except Timeout:
    return "⚠️ Bridge não respondeu (timeout). Tá rodando?"
```

---

## Checklist

- [ ] BigQuery Bridge rodando no PC (`python bigquery-bridge.py`)
- [ ] URL correta no Hermes (seu-pc-ip:5000, não localhost)
- [ ] DREDGE tenta /health primeiro (validação)
- [ ] Se falha → mensagem clara (não tenta adivinhar dados)
- [ ] Se sucesso → estrutura em Markdown tabular

