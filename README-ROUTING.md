# ✅ Roteamento Automático — Pronto

**Seu MAESTRO agora roteia automaticamente.**

## Teste Agora

Vá em CHAT do Hermes e digite **sem @**:

```
"Como tá o time?"
```

Sistema automaticamente roteia pra @maestro-relatorio. MAESTRO responde.

## Como Usar

### Opção 1: Já Funciona (Manual, 0 setup)

Qualquer pergunta sobre time sem @ é roteiada automaticamente via daemon.

```
→ "Como tá hoje?" — roteia
→ "Meta atingida?" — roteia
→ "Performance do João?" — roteia
```

### Opção 2: Skill `/maestro-router` (Setup = 1 minuto)

Se o daemon não estiver rodando, você pode usar:

```
/maestro-router Como tá o time?
```

### Opção 3: Manual (Sempre funciona)

```
@maestro-relatorio Como tá o time?
```

## Instalação (Daemon — Recomendado)

Leia [ROUTING-SETUP.md](./ROUTING-SETUP.md) pra instruções passo-a-passo.

TL;DR:

```bash
# No seu VPS:
sudo systemctl start hermes-router-daemon.service
sudo systemctl enable hermes-router-daemon.service

# Verificar:
sudo systemctl status hermes-router-daemon.service
```

## Palavras-chave Detectadas

**Automáticamente atiram o roteamento:**

- time, status, performance, funil, meta, conversão, ticket, leads, ligações, alertas
- Beatriz, João, Jesiel, Tiago, Ana, Fabiano, Emerson

## Pronto?

- ✅ maestro-router skill criado
- ✅ hermes-router-daemon.py pronto
- ✅ systemd service configurado
- ✅ Documentation completa

**Próximo passo**: escolha uma opção acima e teste.

---

Veja [ROUTING-SETUP.md](./ROUTING-SETUP.md) para detalhes completos.

