#conhecer as estruturas de repetição FOR e WHILE, e quando utilizá-las \n
#exemplo sem repetição:

a = int(input("Informe um numero inteiro: "))

a += 1
print(a)
a += 1
print(a)

#exemplo com repetição:

a = int(input("Informe um numero inteiro: "))
print(a)

#repita 2 vezes:
a += 1
print(a)

#comando FOR é usado para percorrer um objeto iterável. Faz sentido usar o FOR quando sabemos \n
#o numero EXATO de vezes que o nosso bloco de código deve ser executado, ou quando queremos percorrer \n
#percorrer um objeto iterável.
#exemplo:

texto = input("Informe o texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()

#Função RANGE é uma  função built-in do python, ela é usada para produzir uma \n
#sequencia de números inteiros a partir de um ínicio (inclusivo) para um fim (Exclusivo).z \n
#Se usarmos range (i, j) sera produzido:
# i, i+1, i+2, i+3,..., j-1.
#Ele recebe 3 argumentos: stop(obrigatório), start (opcional) e step opcional.

#Exemplo de range(stop) -> range object
#Range(start, stop[, step]) -> range object

list(range(4)) #converteu o range object para uma lista, assim detalhando os steps

#exibindo a tabuada de 5 com o FOR ultilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")


#Comando 'while' é usado para repetir um bloco de código várias vezes. Faz sentido usar \n
#quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.

#Exemplo

opcao = 1 

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, ate logo!")


#exemplo 2

numero = -1 

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break
    
    print(numero)


#exemplo 3


    for numero in range(100):

        if numero == 10:
            break
    
    print(numero, end="")

#exemplo 4 com 'continue' faz com que pule o numero 12
    for numero in range(100):

        if numero == 12:
            continue
    
    print(numero, end="")

