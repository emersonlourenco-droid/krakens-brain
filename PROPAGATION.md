# PROPAGATION.md — Protocolo de Escrita do Krakens Brain

Informação que fica só no chat se perde. Este arquivo define para onde DREDGE e futuros agentes escrevem.

## Regra-Mãe

**Mudou estado? Salve no lugar certo.**

## Tabela de Propagação

| Quando | Escrever em | Formato |
|--------|-------------|---------|
| Nova métrica extraída | `/metricas/dashboard.md` | Tabela Markdown |
| Alerta disparado | `/alertas/YYYY-MM-DD.md` | CSV + resumo |
| Decisão importante | `memory/decisions.md` | Data + contexto |
| Aprendi padrão | `memory/lessons.md` | Sinal + regra |
| Tarefa nova | `memory/tasks.md` | Checklist |
| Ideia de feature | `memory/ideas.md` | Título + descrição |
| Performance de vendedor | `/vendedores/{nome}.md` | Histórico + delta |
| Análise de funil | `/funil/gargalo.md` | Distribuição S1-S9 |

## Regras de Escrita

- ✅ Sempre incluir timestamp
- ✅ Sempre indicar fonte (Google Data Studio, fallback, etc)
- ✅ Valores históricos não são deletados, são arquivados
- ✅ Números brutos + interpretação separados
- ❌ Não salvar logs crus (summarize antes)
- ❌ Não inventar métrica
- ❌ Não duplicar fonte de verdade
- ❌ Não deixar arquivo solto na raiz sem documentação

## Formato de Métrica

```markdown
# Dashboard — YYYY-MM-DD

| Métrica | Valor | Fonte | Status |
|---------|-------|-------|--------|
| GBV | R$ 45.230 | Google Data Studio | ✅ |
| Meta atingida | 78% | Calculado | ✅ |
| Ticket médio | R$ 2.890 | GDS | ✅ |
```

## Formato de Alerta

```markdown
# Alertas — YYYY-MM-DD HH:MM

## 🔴 Crítico
- Beatriz <50% meta (34%)
- João leads >5 dias (7 leads)
- FTR crítico: Jesiel 27min (limite 20)

## 🟡 Aviso
- Emerson ticket abaixo de R$ 2.000
```

## Formato de Decisão

```markdown
## YYYY-MM-DD — [Título]

**Contexto:** Por que isso foi decidido.
**Decisão:** O que vale agora em Krakens.
**Consequência:** O que muda na prática.
**Revisar quando:** Condição de revisão.
**Afeta:** DREDGE / Maestro / Playbook
```

## Histórico de Métricas

- Nunca delete dados históricos
- Se métrica fica obsoleta: `archive/histórico-métrica-antiga.md`
- Cache agressivo = dados de hoje estão em `metricas/dashboard.md`
- Histórico de 30 dias em backup local (fallback)

