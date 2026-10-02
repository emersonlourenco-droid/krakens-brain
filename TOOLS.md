# TOOLS.md — Ferramentas e Permissões do Krakens Brain

Define quais ferramentas cada agente pode usar e com quais restrições.

## Regra-Mãe

> Use ferramenta quando a resposta depender de estado real. Não responda "de cabeça" quando pode verificar.

## DREDGE — Ferramentas Disponíveis

### Permitidas (Sem Aprovação)

| Ferramenta | Uso | Limite |
|---|---|---|
| `google_data_studio` | Ler dashboard em tempo real | Daily refresh |
| `json_read` | Ler `/metricas/dashboard.json` (fallback) | Local apenas |
| `csv_parse` | Parsear alertas históricos | Archive only |
| `markdown_write` | Atualizar `/metricas` e `/alertas` | PROPAGATION.md rules |
| `math_calculate` | Cálculo de %, conversão | Sempre com fonte |

### Não Permitidas

- Deletar qualquer arquivo
- Enviar email/mensagem pública
- Criar agendamento automático (MODO MANUAL)
- Alterar `hermes-config.json`
- Acessar `/vendedores` (só leitura via MAESTRO)

### Integração com Hermes

DREDGE roda em:

```
hermes-config.json
├── agent_configs.dredge
│   ├── enabled: true
│   ├── model: claude-opus-5-5
│   ├── data_source: Google Data Studio URL
│   └── skills: [report-today, report-month, report-seller, report-funnel, alerts-check]
```

Chamada: `@krakens-dredge [pergunta]`

## MAESTRO (Emerson) — Ferramentas Disponíveis

### Permitidas (Sem Aprovação)

| Ferramenta | Uso |
|---|---|
| `read_all` | Ler todo o brain |
| `write_historico` | Salvar decisões em `/historico` |
| `call_dredge` | Chamar DREDGE via Hermes |
| `analyze_data` | Interpretar dados de DREDGE |
| `generate_report` | Compilar report multiagente |

### Permitidas (Com Aprovação)

- Enviar briefing intraday (Slack, Teams, etc)
- Publicar decisão publicamente
- Alterar playbook ou regras de negócio

## Ações Autônomas (DREDGE)

✅ Ler Google Data Studio
✅ Atualizar `/metricas` com novos dados
✅ Disparar alerta em `/alertas`
✅ Registrar lição em `memory/lessons.md`
✅ Estruturar tabela Markdown
✅ Validar números contra histórico
❌ Perguntar tudo de novo (Emerson delegou autoridade)

## Ações com Aprovação

- Deletar dados históricos (move para `archive/` em vez de deletar)
- Criar nova skill (propor a Emerson)
- Mudar dados em `/playbook` (Emerson decide)
- Modificar `hermes-config.json` (só TL)

## Segredos (Nunca Versioná-los)

```
.env
google-credentials.json
hermes-api-key.json
supabase-secret.env
```

Use `.env.example` para mostrar nomes sem valores.

## Integração com BigQuery (Futuro)

Quando ativar qualitativo + Supabase:

```
hermes-config.json
├── agent_configs.scope_codex
│   ├── data_source: Supabase (qualitativo)
│   └── model: claude-opus-5-5
```

PROPAGATION: resultados → `/vendedores/{nome}.md`

