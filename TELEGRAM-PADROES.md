# Telegram @Krakensbot — Padrões de Resposta

## Princípio

Bot responde **números E qualitativo quando você pedir**.  
Nunca aciona por iniciativa própria.

---

## Agora (Phase 1 — Números)

### ✅ Você pede NÚMEROS

```
"Como tá o time?"
→ Bot chama DREDGE
→ Retorna tabela + alertas + insights

"Performance da Beatriz?"
→ Bot chama DREDGE
→ Retorna números (7 dias, gargalo, etc)

"Qual é o gargalo?"
→ Bot chama DREDGE
→ Retorna funil + onde está parado
```

### ❌ Você pede QUALITATIVO (ainda não está pronto)

```
"Por que João tá com FTR alto?"
→ Bot responde: "Isso precisa de análise qualitativa. 
   Estou preparando o SCOPE CODEX para isso. 
   Por enquanto só tenho números. Quer que eu traga?"
```

### ❌ Mensagem genérica (não especifica)

```
"Oi"
→ Bot responde normalmente (não aciona agente)

"Tudo bem?"
→ Bot responde normalmente

"Me ajuda"
→ Bot responde: "Com dados numéricos posso ajudar. 
   Quer saber como tá o time?"
```

---

## Depois (Phase 2 — Qualitativo)

Quando SCOPE CODEX estiver pronto:

```
"Por que João tá com FTR alto?"
→ Bot chama SCOPE CODEX
→ Retorna análise: "Abertura dele tem 2 padrões diferentes, 
  áudio é 60seg (muito longo), cadência é 1/dia (baixa)"

"Análise da Beatriz"
→ Bot chama SCOPE CODEX
→ Retorna: "Beatriz tá com padrão bom em abertura, 
  áudio 25seg (objetivo), cadência 4/dia (alta)"
```

---

## Fluxo de Decisão

```
Mensagem no Telegram
    ↓
É pergunta específica sobre números?
    ├─ SIM → Chama DREDGE
    │        Retorna: tabela + alertas + insights
    │
É pergunta específica sobre qualitativo?
    ├─ SIM → Chama SCOPE CODEX (se pronto)
    │        Retorna: análise qualitativa
    │        Se não pronto: "Ainda não tá pronto"
    │
É mensagem genérica?
    └─ SIM → Responde normalmente
             Não aciona agente
```

---

## Exemplos de Perguntas

### NÚMEROS (Aciona DREDGE)

- "Como tá o time?"
- "Qual é a meta de hoje?"
- "Performance da Beatriz?"
- "Tem alerta?"
- "Quantas ligações hoje?"
- "Qual é o funil?"
- "Ticket médio da semana?"
- "FTR de hoje?"
- "GBV do mês?"
- "Taxa de conversão?"

### QUALITATIVO (Aciona SCOPE CODEX quando pronto)

- "Por que João tá com FTR alto?"
- "Análise da Beatriz"
- "Como melhorar o áudio de Pedro?"
- "Qual vendedor tá com melhor processo?"
- "Por que conversão caiu?"
- "Aberturas estão boas?"

### GENÉRICO (Resposta normal)

- "Oi"
- "Tudo bem?"
- "O que você faz?"
- "Me ajuda"
- "Como você funciona?"

---

## Regra de Ouro

🔴 **Nunca aciona agente por iniciativa**  
✅ **Só quando você pedir especificamente**  
📊 **Números**: DREDGE (agora)  
📝 **Qualitativo**: SCOPE CODEX (depois)

