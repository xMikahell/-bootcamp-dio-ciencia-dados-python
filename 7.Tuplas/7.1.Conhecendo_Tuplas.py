#tuplas são estruturas mais parecidas com as listas, a 
#princinpal diferença e que tuplas são imutaveis enquanto a 
# listas são mutaveis


frutas = ("laranja", "pera", "uva",)

letas = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)


#excesso a uma tupla

frutas = ("maça", "laranja", "pera", "uva",)
frutas[0] #maça
frutas[2] #pera

#tuplas 
#matriz exemplo

matriz = (

    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)


matriz[0] 
matriz[0][0]
matriz[0][-1]
matriz[-1][-1]

#metodos da classe tuple
#().count, ().index, ().len