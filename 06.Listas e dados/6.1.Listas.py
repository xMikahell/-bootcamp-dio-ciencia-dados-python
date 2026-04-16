#Listas em python podem armazenar de maneira sequencial qualquer tipo \n
#de objeto. Listas são objetos mutaveis, portanto podemos alterar seus valores apos a criação

#exemplo:

frutas = ["laranja", "maçã", "uva"]

frutas = []

letras = list ("python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

lista = ["p", "y", "t", "h", "o", "n"]

lista [2:]

lista [:2]
lista [1:3]
lista [0:3:2]
lista [::]
lista [::-1]

#filtro versao 1

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)


#filtro versao 2 

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

#modificando valores versao 1

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

