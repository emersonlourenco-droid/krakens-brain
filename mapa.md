# Mapa do Krakens Brain 🗺️

**Guia de navegação e estrutura do conhecimento**

## O que é este brain?

Este é o **segundo cérebro** do agente TL (Team Lead) - Maestro. Ele contém todo o contexto operacional da Krakens Performance OS.

## Estrutura de pastas

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

## Próximas etapas

⏳ **Aguardando contexto**. Emerson vai preencher cada pasta com:
- Estrutura de dados real
- Templates
- Primeiros registros

---

*Ultimo update: 2026-10-01*
