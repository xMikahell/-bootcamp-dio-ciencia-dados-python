#exemplo de indentação, formatar corretamente o código, melhorando visualmente e com isso o codigo fica organizado

def sacar (valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("Retire o seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia.")

def depositar(valor):
    saldo = 500
    saldo += valor


sacar(1000)