# Feedback Qualitativo — Ana Paula Reczcki (02/10/2026)

## Contexto
- Problema: 80% do pipeline parado em abertura
- FTR: 21 min (deveria ser ~13 min)
- Causa: Abertura não padronizada + Áudio extenso + Cadência baixa

---

## Raiz 1: Abertura Não Padronizada

### Diagnóstico
Ana estava usando **2 aberturas diferentes**:
- Abertura de disparo (antiga)
- Abertura de novo lead

Inconsistência → Leads confusos → Demora pra responder → FTR alto

### Solução Implementada
1. **Descartar abertura de disparo**
2. **Usar só 1 abertura padronizada** — dividida em 2 mensagens:
   - Msg 1: Apresentação + contexto
   - Msg 2: Pergunta de abertura

3. **Escolher abertura com melhor histórico no banco**
   - Não é opinião — é dado de qual abre mais

### Exemplo Bom
```
Msg 1: "Oi, eu sou a Ana, muito prazer. Você conversou com a gente antes, 
       mas a última conversa foi em [data]. Vi que você tem interesse em inglês."

Msg 2: "Como que tá seu nível de inglês hoje? Você já estudou antes?"
```

### Métricas de Sucesso
- FTR volta pra ~13 min
- Taxa de resposta aumenta
- Menos variação de tempo entre leads

---

## Raiz 2: Áudio de Conexão Muito Extenso

### Diagnóstico
Áudio inicial de Ana:
- Muitas desculpas ("desculpa o áudio ruim", "troquei o fone")
- Muito contexto antes do ponto
- Cansativo pra ouvir até o fim

### Solução Implementada

**Manter**: Personalidade (é o diferencial)  
**Cortar**: Tudo que não seja essencial  
**Objetivo**: Áudio 20-30 seg max

#### Estrutura de Áudio Bom
```
[Abertura curta]
"Pô, cara, acho que você tá no lugar certo pra aprender inglês"

[Ponto principal em 1 frase]
"Você quer fazer amigos, viajar, e poder conversar naturalmente"

[Pergunta clara]
"Como que tá seu nível de inglês hoje? Você já estudou?"

[Fim]
```

#### O que Cortar
- ❌ "Desculpas" sobre áudio/fone/problemas técnicos
- ❌ Muito contexto explicativo
- ❌ Múltiplas perguntas no mesmo áudio
- ❌ Fechamentos longos ("então é isso, abraço, etc")

### Padrão: Texto + Áudio

**Sempre que mandar áudio:**
1. Manda **texto primeiro** (cria curiosidade)
2. Depois **áudio** (interesse já existe)

Exemplo:
```
📱 Texto: "Fulano, do que a gente conversou ali, 
           me conta qual dos planos fez mais sentido?"

🎙️ Áudio: [Áudio reforçando a pergunta]
```

Por que funciona:
- Lead lê texto → cria expectativa
- Lead escuta áudio → confirmação + personalidade
- Lead responde → engagement maior

---

## Raiz 3: Cadência de Follow-up Baixa

### Diagnóstico
Ana estava fazendo: **1 follow por dia**  
Deveriam ser: **3-4 follows de intraday**

Resultado: Leads esquecem, oportunidade perde

### Solução Implementada

#### Estrutura de Follow-up (3 toques)

**1º Follow** (Lateralidade — Objetivo)
```
"Me conta, por que que é importante pra você aprender inglês?
O que você busca num curso de idiomas?"
```

**2º Follow** (Lateralidade — Validação)
```
"Ótimo! Então você quer fazer amigos, viajar, e conversar naturalmente.
Como que tá seu nível de inglês pra isso?"
```

**3º Follow** (Metodologia + Preço)
```
"Beleza, então a gente trabalha assim: 10 meses de plano,
fluência garantida. Temos duas opções: R$249 ou R$399.
Qual se encaixa melhor na sua rotina?"
```

#### Timing Intraday (sem lead responder)
| Hora | Tipo | Conteúdo |
|------|------|----------|
| D0 + 2h | Texto | 1º Follow (Objetivo) |
| D0 + 4h | Áudio | Reforço com personalidade |
| D0 + 8h | Texto | 2º Follow (Validação) |
| D0 + 24h | Áudio | 3º Follow (Metodologia) |

### Regra de Ouro
- **Se lead não responde em D0**: Não abandona
- **Se lead não responde em D1**: Reavalia ângulo (S8/S9)
- **Nunca só 1 toque/dia**

---

## 4. Processo de Abertura (Resumido)

### Checklist Diário (Retomar)

```
☐ Leads em abertura (S1-S3)
  ☐ 1º toque: Abertura padronizada
  ☐ 2º toque: Follow de objetivo
  ☐ 3º toque: Follow de conexão
  
☐ Leads em conexão (S4-S5)
  ☐ Acompanhar resposta
  ☐ Fazer pergunta complementar (consultivo)
  
☐ Leads em fechamento (S6-S7)
  ☐ Passar preço (sem medo)
  ☐ Propor plano
  ☐ Fechar ou encerrar (S8/S9)
```

### Fluxo Baixo-para-Cima (NÃO por etapa)
- ❌ NÃO filtra por etapa (abertura, conexão, fechamento)
- ✅ SIM segue cada lead do mais recente pro mais antigo
- Resultado: Mantém todo pipeline "quente"

---

## 5. Abordagem de Venda Consultiva

### Diferença: Transacional vs Consultivo

**Fechamento (Transacional)**:
```
"Qual sua dúvida da metodologia?
Vagas estão acabando, vamos!"
```

**Abertura/Conexão (Consultivo)**:
```
"Eu não tô aqui pra vender.
Eu tô aqui pra entender como eu te ajudo.

Como que tá seu nível hoje?
Por que isso é importante pra você?"
```

**Analogia**: Médico do SUS (direto: "tome soro") vs Médico particular (pergunta: "quando começou? onde dói?")

### Prática em Áudio
- Fazer pergunta simples
- Aguardar resposta
- Reforçar o objetivo dele
- Só depois propor solução

---

## 6. Próximas Métricas a Acompanhar

Após implementar feedback:

| Métrica | Antes | Meta |
|---------|-------|------|
| FTR (abertura) | 21 min | ~13 min |
| Resposta em 2h | ? | >40% |
| Taxa de avanço (S1→S2) | ~20% | >60% |
| Fechamentos por semana | ? | +2-3 |
| Cadência média | 1/dia | 3-4/dia |

---

## 7. Implementação

### Semana 1
- [ ] Adotar abertura padronizada (nova)
- [ ] Reativar checklist diário
- [ ] Treinar áudios mais curtos
- [ ] Começar cadência intraday (3-4 toques)

### Semana 2
- [ ] Validar FTR em abertura
- [ ] Revisar áudios com Gisel
- [ ] Confirmar que lead avança (S1→S2 aumentando)
- [ ] Alinhar próximos ajustes com Emerson

---

## 8. Pontos-Chave para o Agente (Treinamento)

Quando SCOPE CODEX analisar um vendedor com:
- **80%+ do pipeline em abertura** → investigar:
  1. Quantas aberturas diferentes usa?
  2. Qual é a melhor do histórico?
  3. Padronizar + validar FTR

- **FTR >15 min em abertura** → investigar:
  1. Áudio é muito longo? (>45seg)
  2. Tem muitas desculpas/contexto?
  3. Personalidade? (manter + objetividade)

- **Cadência <3/dia** → prescrever:
  1. Ativar 3-4 toques intraday
  2. Texto sempre acompanha áudio
  3. Manter lateralidade (perguntas abertas)

---

**Racional Resumido**:
Abertura ruim → FTR alto → lead não avança  
Áudio longo → Lead não completa escuta  
Cadência baixa → Lead esquece  

**Solução**: 1 abertura padrão + áudio curto + 3-4 follows = conversão ✅

