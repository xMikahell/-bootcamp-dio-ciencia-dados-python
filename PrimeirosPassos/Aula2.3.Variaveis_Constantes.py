# Aula 2.3 - Variáveis e entrada de dados
# Exemplos e exercícios do bootcamp

# 1. Exemplo de saque simples (meu experimento)
saldo = 100000
saque = int(input('Digite o quanto você quer sacar: '))
resultado = saldo - saque
print(f"Saldo atualizado é de :R${resultado}")

# 2. Atribuição múltipla e variáveis
nome = "Mikael"
idade = 31

nome, idade = "Giovanna", 27
print(nome, idade)

limite_saque_diario = 1000
BRAZILIA_STATES = ["SP", "RJ", "SC", "PE"]
print(BRAZILIA_STATES)

# 3. Exercício pedido pelo professor
alterarNome = input('Altere o nome existente: ')
nome = alterarNome
print(f"Seu nome agora é {nome}")




