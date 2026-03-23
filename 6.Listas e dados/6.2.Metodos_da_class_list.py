#[].append adicona um novo elemento a lista
#exemplo

list = []

list.append(1)
list.append("Python")
list.append([40, 30, 20])

print(list)


#[].clear apagar elementos da lista
#exemplo

lista = [1, "Python", [40, 30,20]]

print(lista)

lista.clear()

print(lista)

#[].copy 

lista = [1, "Python", [40, 30,20]]

l2 = lista.copy()

print(lista)
print(id(l2), id(lista))

l2[0] = 2

print(l2)
print(lista)

#[].count

cores = ["vermelho", "azul", "verde","azul"]

cores.count("vermelho")
cores.count("azul")
cores.count("verde")


#[].extend 

linguagens = ["python", "js", "c"]

print(linguagens)

linguagens.extend

#[].index

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.index("java")
linguagens.index("python")

#[].pop

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.pop()
linguagens.pop()
linguagens.pop()
linguagens.pop(0)

#[].sort

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)

#len 

linguagens = ["python", "js", "c", "java", "csharp"]
len(linguagens)

#sorted

linguagens = ["python", "js", "c", "java", "csharp"]
sorted(linguagens, key= lambda x: len(x))

sorted(linguagens, key= lambda x: len(x), reverse=True)

