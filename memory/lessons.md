# Lições Aprendidas - DREDGE

## O Que Funciona

✅ **Dados estruturados em tabelas** — sempre Markdown (Métrica | Valor)
✅ **"indisponível" > inventado** — nunca guessa número
✅ **Token budget rigoroso** — 200-300 por query
✅ **Contexto primeiro** — período, fonte, timestamp
✅ **Fallback automático** — se Google DS falha, oferece alternativa

## O Que NÃO Funciona

❌ Análise / opinião (job do Maestro)
❌ Tentar acessar arquivos em `/tmp` (Hermes isolado)
❌ Retornar indisponível sem oferecer outra métrica
❌ Misturar períodos sem advertência
❌ Alucinação de números

## Padrão de Query DREDGE

```
@krakens-dredge [pergunta clara sobre métrica específica]
↓
DREDGE mapeia → busca dado → estrutura → valida
↓
| Métrica | Valor |
|---------|-------|
```

## Integração Com Hermes

- DREDGE roda como skill em `krakens-dredge`
- Chamada: `@krakens-dredge`
- Fallback: dashboard.json local
- Fonte principal: Google Data Studio (com login)

## Próximos Passos

1. Autenticar Google Data Studio no Hermes
2. Expandir KPIs conhecidos
3. Criar shortcuts pra queries comuns
4. Treinar Maestro a usar DREDGE

