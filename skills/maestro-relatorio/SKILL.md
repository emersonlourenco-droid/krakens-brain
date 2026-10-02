---
name: maestro-relatorio
description: Relatórios estruturados do time por período (dia, semana, mês) com alertas e plano de ação
---

# Skill: Maestro Relatório

**Use quando:** O usuário perguntar "como tá o time?", "qual é o status?", "quem tá abaixo da meta?", "como tá a Beatriz?"

## O que faz

Traz relatórios estruturados com:
- Ligações, leads recebidos, taxa de conversão
- Ticket médio e % venda cheia
- Distribuição do funil (gargalos)
- Alertas em vermelho (ticket < R$ 2.450, venda cheia < 65%, meta < 100%)
- Plano de ação (quinta/sexta)

## Período Automático

- **Segunda** → Semana anterior (passada)
- **Terça/Quarta** → Dia anterior + Dia atual
- **Quinta/Sexta** → Semana toda + Plano de ação

## Chamada

```
"Como tá o time hoje?"
→ MAESTRO chama DREDGE pra trazer dados
→ Formata relatório estruturado

"Como tá a Beatriz?"
→ Relatório individual com mesmas métricas
```

## Saída

Tabelas limpas com:
- Métricas chave (ligações, conversão, ticket)
- Funil (com % e gargalos)
- Alertas em 🔴
- Plano de ação (quinta/sexta)

## Exemplo

```
🎯 BEATRIZ DUTRA — TERÇA, 30/09

📊 HOJE + SEMANA
├─ Ligações: 8 hoje | 45 semana
├─ Taxa de conversão: 7,00%
├─ Ticket médio: R$ 2.800 ✅
├─ Meta: R$ 123.480 | 108% ✅
└─ FUNIL:
   ├─ Abertura: 92 (37%)
   └─ Fechamento: 104 (41%) ← ACÚMULO

🚨 ALERTAS: Nenhum (ok)
```

---

**Prompt:** Ver `prompts/maestro-relatorio-prompt.md`

