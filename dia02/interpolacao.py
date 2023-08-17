email_tmpl = """Olá, %(nome)s

Tem interesse em comprar o produto %(produto)s?

Este produto é ótimo para resolver %(texto)s

Clique agora em %(link)s

Apenas %(quantidade)d disponíveis!

Preço promocional %(preco).2f
"""

clientes = ["João", "Maria", "José"]

for cliente in clientes:
    print(email_tmpl % {"nome": cliente,
                        "produto": "caneta",
                        "texto": "escrever muito bem",
                        "link": "https://canetaslegais.com",
                        "quantidade": 2,
                        "preco": 50.5
                        })
    
