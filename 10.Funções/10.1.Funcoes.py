#Função, é um bloco de código identificado por um nome e pode
# receber uma lista de parâmetros, esses parâmetros, esses parâmetros podem
# ou não ter valores padrões.

#Ex.:

def exibir_mensagem():
    print("Olá Mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo{nome}!")

def exibir_mensagem_3(nome="Mikael"):
    print(f"Seja bem vindo {nome}!")

#Retornando valores
#Para Retornar um valor, utilizamos a palavra reservada return.
#Toda função retorna None por padrão. Diferente de  outras linguagens de 
#programação, em Python uma função pode retornar mais um valor. 

#Exemplo

def calcular_total(numeros):
    return sum(numeros)

def retornar_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def func_3():
    print("Olá Mundo!")


print(calcular_total([10, 20, 34]))
print(retornar_antecessor_e_sucessor(10))
print(func_3())


#Argumnento Nomeado
#Funções também podem ser chamadas usando argumentos nomeados de forma chave=valor

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Celta", 2000, "ACC-1234")
salvar_carro(marca="Fiat", modelo="Celta", ano=2000, placa="ACC-1234")
salvar_carro(**{"marca": "Fiat", "marca": "Celta", "ano" : 2000, "placa": "ACC-1234"})


#Args e Kwargs
#Podemos combinar parâmetros obrigátorios com args kwargs. Quando esses são difinidos (*args e **Kwargs),
#o método recebe os valores como tupla e dicionário respectivamente

#exemplo


def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.tittle()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso} \n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Zen of Python", "Beautiful is than Ugly.", autor="Tim Peters", ano=1999)


#Parâmetros especiais
# Por padrão, argumentos podem ser passado para uma função Pyhton tanto
#por posição quanto explicitamente pelo nome.
#Para uma melhor legibilidade e  desempenho, faz sentido restringir a maneira pelo qual
#argumentos possam ser passados, assim um desenvolvedor precisa apenas olhar para a 
#definição da função para determinar  se os itens são passados
#por posição, por posição e nome, ou por nome.

#Keyword Only

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ACC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")


#objestos de primeira classe.
#Em Python tudo é objeto, dessa forma as funções também são objetos o que 
#as tornam objetos de primeira classe. Com isso podemos atribuir funções a variaveis
#passá-las como parâmetro para funções, usa-las como valores em estruturas de dados
#(listas, tuplas, dicionários, etc) e usar como valor de retorno para uma função(closures).

#exemplo

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)

op = somar

print(op(1, 23))

#Escopo local e escopo global
#Python trabalha com escopo local e global, dentro do bloco da função
#o escopo é local. Portanto alterações  ali feitas em objetos imutavéis 
#serão perdidasq quando o método terminar de ser executado. Para usar objetos
#exemplo 

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_com_bonus = salario_bonus(500)
print(salario_com_bonus)

#exemplo 2

salario2 = 3000

def salario2_bonus(bonus, lista):
    global salario2

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")

    salario2 += bonus
    return salario2

lista = [1]
salario2_com_bonus = salario2_bonus(600, lista)
print(salario_com_bonus)
print(lista)

