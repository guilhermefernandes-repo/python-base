# Concatenação %s --> Logging
# str.format {} --> Mensagens longs, e-mail
# f-strings --> Restante, mensagens, print, error

email_tmpl = """
Olá, %(nome)s

Tem interesse em comprar %(produto)s?

Este produto é ótimo para resolver
%(texto)s

Clique agora em %(link)s

Apenas %(quantidade)d disponíveis!

Preço promocional %(preco).2f
"""

clientes = ["Maria", "João", "Bruno"]

for cliente in clientes:
    print(email_tmpl % {"nome": cliente,
    "produto": "Caneta Bic",
    "texto": "Escrever muito bem",
    "link": "https://canetaslegais.com.br",
    "quantidade": 1,
    "preco": 50.5
    }
    )
