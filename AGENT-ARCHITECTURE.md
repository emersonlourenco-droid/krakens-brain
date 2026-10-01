# Arquitetura de Agentes - Krakens TL

## Princípios
- **Zero genérico**: Cada agente é específico ao contexto Krakens
- **Token-efficient**: Prompts curtos, contexto recuperado, caching agressivo
- **Output-focused**: Cada agente tem um output concreto e acionável
- **Sem alucinações**: Baseado em dados, não em inferências

## Agentes Ativos (v1)

### 1. **DREDGE** - Data Extractor & Reporter
**Responsabilidade**: Extrair dados quantitativos e gerar reports
**Entrada**: 
- `/metricas/dashboard.json` (empresa.knowledge-base)
- Query de período/vendedor (do usuário)

**Output**: 
- Report estruturado (KPIs, metas, performance)
- Formato: Markdown tabular + insights curtos

**Token Economy**:
- Cache: dashboard.json inteiro (não muda diariamente)
- Retrieval: Query-specific (só puxa seções relevantes)
- Prompt: ~300 tokens (fixed)
- Output: ~500-800 tokens (depende da query)

**Exemplo de Uso**:
```
User: "Como tá a performance de hoje?"
Dredge: 
- Lê dashboard.json (cached)
- Extrai KPIs de 2026-10-01
- Retorna: GBV, Meta%, Ticket, Pipeline, FTR
- Formato: Tabela + 2-3 insights
```

---

## Agentes em BACKUP (para ativar depois)

### 2. **SCOPE CODEX** - Qualitative Analyzer
**Responsabilidade**: Analisar conversas, qualidade, gargalos
**Entrada**: Transcrições de conversas, Supabase
**Status**: BACKUP (não ativar ainda)
**Config**: Em `agentes/scope-codex-backup.json`

### 3. **UNDERTOW CODEX** - Quality Auditor
**Responsabilidade**: Auditar processos, compliance, rubricas
**Status**: BACKUP (não ativar ainda)
**Config**: Em `agentes/undertow-codex-backup.json`

---

## Configuração Hermes

**Main Agent**: `maestro-tl`
- Orquestra DREDGE
- Responde perguntas
- Mantém histórico de decisões

**DREDGE Config**:
```json
{
  "name": "dredge",
  "type": "data-extractor",
  "sources": ["metricas/dashboard.json"],
  "cache_strategy": "aggressive",
  "retrieval": "query-specific",
  "output_format": "markdown-tabular"
}
```

---

## Próximas Etapas
1. ✅ Criar Skills de DREDGE (específicas Krakens)
2. ✅ Conectar dashboard.json como source
3. ⏳ Treinar DREDGE com queries reais
4. ⏳ Ativar SCOPE CODEX (quando Supabase estiver ready)
5. ⏳ Ativar UNDERTOW CODEX (quando rubrica estiver validada)
