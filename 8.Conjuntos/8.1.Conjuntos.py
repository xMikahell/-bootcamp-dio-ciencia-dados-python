#Um set é um coleção que não possuo objetos repetidos, 
#usamos sets para representar conjuntos matematicos ou 
# eliminar itens duplicados de um iteravel


set([1, 2, 3, 4, 5, 1, 2, 3,])

set("abacaxi")

set(("palio", "gol", "celta", "palio"))


#exemplo 1

numeros = set([1, 2, 3, 4, 5, 1, 2, 3,])
print(numeros)

letras = set("abacaxi")
print(letras)

carros = set(("palio", "gol", "celta", "palio"))
print(carros)

linguagens = {"python", "java", "python"}
print(linguagens)

#Conjuntos em python não suportam  indexação(.index) e nem fatiamento, caso queira
#acessar seus valores é necessário converter o conjunto para lista

#exemplo
numeros = {1, 2, 3, 4, 5, 1, 2, 3}

numeros = list(numeros)

print = (numeros[0])


#For

carros = set(("palio", "gol", "celta"))
for carro in carros:
    print(carro)


#Função enumerate 
#Às vezes é necessario saber qual o indice do objeto dentro do laço FOR
#para isso podemos usar a função enumerate

carros = set(("palio", "gol", "celta"))
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#Metodos da classe set
#{}.union

conjunto_a = {1, 2} 
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b)

#{}.intersection 

conjunto_a = {1, 2, 3} 
conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b)

#{}.difference 

conjunto_a = {1, 2, 3} 
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b)
conjunto_b.difference(conjunto_a)

#{}.symmetric_difference

conjunto_a = {1, 2, 3} 
conjunto_b = {2, 3, 4}

conjunto_a.symmetric_difference(conjunto_b)

#{}.issubset
conjunto_a = {1, 2, 3} 
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) #true
conjunto_b.issubset(conjunto_a) #false

#{}.issuperset
conjunto_a = {1, 2, 3} 
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) #false
conjunto_b.issubset(conjunto_a) #true

#{}.isdisjoint
conjunto_a = {1, 2, 3, 4 , 5,} 
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b) #True
conjunto_a.isdisjoint(conjunto_c) #false
 
#{}.add

sorteio = {1, 23}

sorteio.add(25)
sorteio.add(42)
sorteio.add(25)

#{}.clear

sorteio = {1, 23}

sorteio.clear()

#{}.copy

sorteio = {1, 23}
sorteio
sorteio.copy()

#{}.discard

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros
numeros.discard(1)
numeros.discard(45)

#{}.pop

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros
numeros.pop()
numeros.pop()
numeros

#{}.remove
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros
numeros.remove(0)

#{}.len

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

len(numeros)

#in

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

1 in numeros #true
10 in numeros #false



