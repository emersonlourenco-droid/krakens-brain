# Hermes Routing Instruction — Automático MAESTRO

**Cole isso no CONFIG do Hermes (Agent section) como "System Instruction":**

```
Se a pergunta do usuário contiver qualquer uma dessas palavras-chave:
- time, status, performance, funil, meta, conversão, ligações, leads, ticket, alertas
- OU nomes de vendedor: Beatriz, João, Jesiel, Tiago, Ana, Fabiano, Emerson

AUTOMATICAMENTE:
1. Roteia pra @maestro-relatorio
2. Passa a pergunta inteira
3. Retorna o resultado do MAESTRO
4. NÃO necesita @ na pergunta do usuário

EXEMPLO:
User: "Como tá o time?"
System: (deteta "time")
System: Chama @maestro-relatorio "Como tá o time?"
System: Retorna relatório do MAESTRO

User: "Performance da Beatriz?"
System: (detecta "Beatriz")
System: Chama @maestro-relatorio "Performance da Beatriz?"
System: Retorna dados de Beatriz
```

## Como adicionar no Hermes

1. Ir em CONFIG
2. Clicar em "Agent" (esquerda)
3. Procurar por "System Instruction" ou "System Prompt"
4. Colar essa regra
5. Salvar

Pronto! Automático.
