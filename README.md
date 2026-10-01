# Krakens Brain 🧠

**Second Brain para o Agente TL (Team Lead) - Krakens Performance OS**

Este é o repositório centralizado de conhecimento para orquestração de agentes no Hermes, estruturado como um "segundo cérebro" que alimenta o agente TL com contexto profundo sobre operações da empresa.

## Estrutura

```
krakens-brain/
├── vendedores/          # Perfil, histórico e performance de cada vendedor
├── playbook/            # Regras de negócio, estratégias, decisões críticas
├── metricas/            # KPIs, dashboard, dados de performance
├── historico/           # Decisões, pivots, aprendizados
├── funil/               # Classificação S1-S9, gargalos, análise
├── alertas/             # Condições críticas que disparam ações
└── agentes/             # Orquestração de agentes (Dredge, Scope, Undertow, Maestro)
```

## Como funciona

1. **Hermes + GitHub**: O agente TL lê este repositório diariamente via Compose.dev/GitHub API
2. **Mapa.md**: Define as relações entre arquivos e contextos
3. **Auto-update**: Agentes atualizam dados em tempo real (métricas, decisões, alertas)
4. **Consultas**: TL consulta este brain para gerar reports e insights

## Próximos passos

⏳ Aguardando contexto do usuário para preencher as pastas com dados.

---

*Criado para: Emerson | Krakens Performance OS*
