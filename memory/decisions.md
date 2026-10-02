# Decisões Arquiteturais

## Por que SOUL.md?

SOUL.md define a identidade imutável de DREDGE. Sem ele, o agente fica:
- Genérico
- Inconsistente
- Propenso a alucinação

Com SOUL.md, DREDGE sabe:
- Quem é (extrator de dados, não analista)
- O que faz (tabelas precisas)
- O que NÃO faz (análise, interpretação)

## Por que "indisponível"?

Alternativa: tentar inferir / adivinhar

Custo: credibilidade e confiabilidade

DREDGE escolhe: precisão > completude

## Por que Google Data Studio + fallback?

Primary: dados live
Fallback: funciona offline

Redundância = robustez

