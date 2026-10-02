# MAPA.md — Navegação do Krakens Brain 🗺️

Este é o **segundo cérebro** de Emerson (TL) e seus agentes: DREDGE, SCOPE CODEX, UNDERTOW CODEX, MAESTRO.

## Bootloader (Leia Neste Ordem)

1. **AGENTS.md** — contrato operacional
2. **SOUL.md** — identidade de DREDGE
3. **USER.md** — quem é Emerson
4. **MAPA.md** ← você está aqui
5. **hermes-config.json** — integração com Hermes
6. **memory/** — decisões curadas (se autorizado)

Não carregue tudo. Root files são roteadores; detalhes entram sob demanda.

## Estrutura Completa

### 📊 `/metricas`
**O que tem**: KPIs do dia, meta, performance, ticket médio, GBV, funil
- Consultado para: Reports diários, análise de performance
- Atualizado por: Dredge (extração de dados)
- Frequência: Real-time / Diário

### 👥 `/vendedores`
**O que tem**: Perfil de cada vendedor, performance individual, gargalos
- Consultado para: Análise individual, sugestões de ação
- Atualizado por: Scope Codex (análise)
- Frequência: Diário

### 📋 `/playbook`
**O que tem**: Regras de negócio, estratégias, critérios de decisão
- Consultado para: Validação de ações, direcionamento
- Atualizado por: Maestro (quando há pivots)
- Frequência: Semanal/conforme necessário

### 🎯 `/funil`
**O que tem**: Classificação S1-S9, análise de gargalos, Megazord
- Consultado para: Entender bloqueios, priorização
- Atualizado por: Undertow Codex (auditoria)
- Frequência: Real-time

### 📖 `/historico`
**O que tem**: Decisões tomadas, pivots, aprendizados, por que mudamos
- Consultado para: Contexto histórico, precedentes
- Atualizado por: Maestro (logger de decisões)
- Frequência: Conforme decisões são tomadas

### 🚨 `/alertas`
**O que tem**: Condições críticas (alguém <50% meta, leads >5 dias, etc)
- Consultado para: Disparar ações urgentes
- Atualizado por: Dredge (monitoramento)
- Frequência: Real-time

### 🤖 `/agentes`
**O que tem**: Documentação de cada agente (Dredge, Scope, Undertow, Maestro)
- Dredge: Extrator de dados
- Scope Codex: Analisador de performance
- Undertow Codex: Auditor de qualidade
- Maestro: Orquestrador/Decisor

## Fluxo de dados

```
Dados brutos (OmniChat, etc)
    ↓
[Dredge] → /metricas, /alertas
    ↓
[Scope Codex] → /vendedores, /funil
    ↓
[Undertow Codex] → /funil (auditoria)
    ↓
[Maestro TL] ← Lê tudo + /playbook
    ↓
Reports + Decisões → /historico
```

## Como o Maestro usa isso?

1. **Consultoria**: Lê este brain antes de gerar reports
2. **Contexto**: Usa /historico para entender precedentes
3. **Decisões**: Valida contra /playbook
4. **Ações**: Dispara baseado em /alertas
5. **Aprendizado**: Atualiza /historico com novas decisões

## Status de Agentes

### 🟢 DREDGE (ATIVO)
- Conectado ao: Google Data Studio
- Skills: report-today, report-month, report-seller, report-funnel, alerts-check
- Modo: Token-efficient com cache agressivo
- Output: Markdown tabular (só dados, zero análise)

### 🟡 SCOPE CODEX (BACKUP)
- Aguardando: Integração Supabase
- Função: Análise qualitativa de conversas

### 🟡 UNDERTOW CODEX (BACKUP)
- Aguardando: Validação de rubrica
- Função: Auditoria de qualidade

## Como usar DREDGE

```
"Que tal a performance de hoje?"
→ report-today: GBV, Meta%, Ticket, FTR, Leads, Ligações, Meetings

"Performance da Beatriz?"
→ report-seller: Números individuais (GBV, Meta%, FTR, etc)

"Tem algum alerta?"
→ alerts-check: Só vermelho (vendedores <50% meta, leads >5d, FTR crítico)
```

---

## Como Agentes Leem Este Brain

### DREDGE (Quantitativo)

1. Leia SOUL.md (identidade)
2. Leia AGENTS.md (ciclo de decisão)
3. Consulte skill relevante (`report-today`, `report-month`, etc)
4. Busque em `/metricas` ou Google Data Studio
5. Estruture em Markdown tabular
6. Atualize `/metricas` e `/alertas`

### MAESTRO (Você)

1. Leia AGENTS.md + SOUL.md + USER.md
2. Leia MAPA.md (você está aqui)
3. Chame DREDGE via `@krakens-dredge` [pergunta]
4. Interprete + decida + aja
5. Atualize `/historico` com decisão

### SCOPE CODEX (Qualitativo — BACKUP)

1. Leia SOUL.md (quando ativar)
2. Consulte `/vendedores` e `/funil`
3. Analise conversas em Supabase
4. Atualize scores de qualidade

### UNDERTOW CODEX (Auditoria — BACKUP)

1. Leia SOUL.md
2. Valide rubrica de qualidade
3. Atualize `/funil` com findings
4. Dispare alertas se necessário

---

*Última atualização: 2026-10-02 | DREDGE + MEMORIA CURADA ATIVA*
