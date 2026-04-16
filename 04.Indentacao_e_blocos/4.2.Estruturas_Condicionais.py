#aula dividida em 3 etapas
#primeira etapa IF/IF-ELSE/ELIF
#segunda etapa if alinhado
#terceira etapa if ternário

#Estrutura condicionais permitem o desvio do fluxo de controle, quando \n
#determinadas expressões logicas são atendidas.

#Etapa 1: if/if-else/elif

#IF usado para criar uma estrutura condicional simples, composta por um unico desvio, podemos \n
#utilizar a palavras reservada 'if'.
#exemplo:

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")

#If/else: usados para criar uma estrutura condicional com dois desvios, podemos \n
#utilizar as palavras reservadas if e else. Se o if for verdadeiro sera executado, caso contrario o codigo else que sera executado.
#exemplo:

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

else:
    print("Saldo insuficiente!")

#elif: usado  em alguns cenários quando queremos mais de dois desvios, para isso podemos utilizar \n
#a palavra reservada 'elif'.
#exemplo

opcao = int(input("Informe uma opção: [1] SACAR \n[2] Extrato: "))

if opcao == 1:
    valor = floar(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo extrato...")

else: 
    print("Opção invalida")



#exemplos:
#IF

MAIOR_IDADE = 18

idade = int(input("Infomer sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar CNH.")


#if/else

MAIOR_IDADE = 18

idade = int(input("Infomer sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

else:
    print("Ainda não pode tirar CNH.")


#if/else/elif

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Infomer sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas e sem aulas praticas")

else:
    print("Ainda não pode tirar CNH.")

#if alinhado 

conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 2500
chaque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso.")
    elif saque <= (saldo + chaque_especial):
        print("Saque realizado com uso do cheque especial.")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente.")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso.")
    else:
        print("Saldo insuficiente.")
else:
    print("O sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")


#if ternário permite escrever uma condição em uma unica linha.
#exemplo
saldo = 5000
saque = 1000

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")



































