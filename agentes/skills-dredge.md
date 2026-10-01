# Skills do DREDGE - Agente Quantitativo Krakens

## 1. report-today
**Descrição**: Performance de hoje em números

**Prompt**:
```
Extraia do Google Data Studio (2026-10-01):
- GBV de hoje
- % da meta de hoje
- Ticket médio
- Pipeline (leads em aberto)
- FTR (primeira resposta em minutos)
- Total de leads recebidos
- Ligações realizadas
- Meetings agendadas

Formato: Tabela com 2 colunas (Métrica | Valor)
Máximo: 200 tokens
Se algum dado não estiver visível, escreva "indisponível"
```

---

## 2. report-month
**Descrição**: Performance acumulada do mês

**Prompt**:
```
Extraia do Google Data Studio (acumulado até 2026-10-01):
- GBV mês
- % da meta mês
- Antecipável (se houver)
- Vendas cheia vs com recorrência
- Conversão (M0, M1, etc)
- Velocity (leads/conversão)

Formato: Tabela com 2 colunas (Métrica | Valor)
Máximo: 250 tokens
Se faltarem dados, use "indisponível"
```

---

## 3. report-seller
**Descrição**: Performance individual (por vendedor)

**Prompt**:
```
Extraia do Google Data Studio para [SELLER_NAME]:
- GBV individual
- % da meta individual
- Ticket médio
- FTR
- Ligações (período)
- Meetings (período)
- Pipeline (leads em aberto)
- Motivo maior de perda (se disponível)

Formato: Tabela com 2 colunas (Métrica | Valor)
Máximo: 300 tokens
Se vendedor não existir, retorne "Vendedor não encontrado"
```

---

## 4. report-funnel
**Descrição**: Funil e gargalos

**Prompt**:
```
Extraia do Google Data Studio:
- Total de chats
- Distribuição por estágio (Abertura, Conexão, Entrega, Fechamento, Link, FUP)
- Estágio com maior concentração
- Maior motivo de perda

Formato: 
- Total: XXX chats
- Distribuição: (usar lista)
- Gargalo: [estágio]
- Perda: [motivo]

Máximo: 250 tokens
```

---

## 5. alerts-check
**Descrição**: Condições críticas

**Prompt**:
```
Verifique no Google Data Studio:
1. Vendedores com <50% meta
2. Leads parados >5 dias
3. FTR crítico (>30min)
4. Ligações do dia (zero = alerta)

Formato:
🚨 ALERTAS:
- [Tipo]: [Detalhes]

Se nada crítico: "Sem alertas críticos"
Máximo: 200 tokens
```

---

## Padrões Obrigatórios
- **Nunca invente dados**
- **Se indisponível, escreva "indisponível"**
- **Sempre Markdown**
- **Máximo de tokens cumprido**
- **Nenhuma análise** — só números

