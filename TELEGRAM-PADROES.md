# Padrões Telegram — @Krakensaloudbot

## Quando Aciona DREDGE (Números)

✅ **DREDGE é acionado automaticamente** quando você pergunta sobre:

```
"Como tá o time?"
"Qual é a meta de hoje?"
"Performance da Beatriz?"
"Tem alerta?"
"Quantas ligações?"
"Qual é o funil?"
"Ticket médio?"
"FTR de hoje?"
```

Qualquer coisa sobre **números, performance, métricas** → DREDGE

---

## Quando NÃO Aciona DREDGE (Conversas)

❌ **NÃO aciona DREDGE** para:

```
"Oi bot"
"Tudo bem?"
"Me ajuda com algo"
"O que você faz?"
"Explica isso pra mim"
```

Qualquer coisa que **não é sobre números** → responde normalmente ou rota pra outro agente

---

## Fluxo

```
Pergunta no Telegram
    ↓
É sobre NÚMEROS/PERFORMANCE?
    ├─ SIM → Chama DREDGE (via BigQuery Bridge)
    │        Retorna tabela + alertas + insights
    │
    └─ NÃO → Responde normalmente
             Ou rota pra outro agente conforme necessário
```

---

## Exemplos

### ✅ Aciona DREDGE

```
"Como tá o time?" 
→ DREDGE puxa /krakens/hoje
→ Retorna tabela com todos vendedores

"Performance da Beatriz?"
→ DREDGE puxa /krakens/vendedor/Beatriz
→ Retorna números últimos 7 dias

"Qual é o gargalo?"
→ DREDGE puxa /krakens/funil
→ Retorna distribuição S1-S9 + onde tá parado
```

### ❌ NÃO Aciona DREDGE

```
"Oi"
→ Responde: "E aí! Sou o bot dos Krakens. Posso puxar dados de performance, números do time, etc."

"Como vai?"
→ Responde: "Tudo certo! Qualquer dúvida sobre números do time, é só chamar"

"Me ajuda a treinar vendedor"
→ Responde: "Isso é com o pessoal de operação. Precisa de dados? Posso trazer números"
```

---

## Implementação

No `telegram-bridge.py`:

```python
def is_dredge_question(message):
    """Detecta se pergunta é sobre números"""
    keywords = [
        'time', 'performance', 'meta', 'quanto', 'qual', 
        'hoje', 'semana', 'mês', 'gbv', 'ticket', 'ftr',
        'ligações', 'meetings', 'conversão', 'funil', 'alerta',
        'vendedor', 'beatriz', 'joão', 'tiago', 'ana', 'jesiel'
    ]
    return any(kw in message.lower() for kw in keywords)

# Se é pergunta sobre números:
if is_dredge_question(user_message):
    response = call_dredge(user_message)
else:
    response = "Resposta genérica ou não aplica DREDGE"
```

---

## Regra de Ouro

**DREDGE = números**  
**Tudo mais = outros agentes ou resposta padrão**

