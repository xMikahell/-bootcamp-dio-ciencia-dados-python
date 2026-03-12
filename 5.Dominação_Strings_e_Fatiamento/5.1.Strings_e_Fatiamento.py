#Metodos uteis da classe String
#Maiúsculo, minúsculo e título

#exemplo

curso = "python"

print(curso.upper())
print(curso.lower())
print(curso.title())

#elinimando espaço em branco
#exemplo

curso = "       Python"
print(curso.strip())  #remove os espaços do Inicio e fim
print(curso.lstrip()) #remove espaço da esquerda
print(curso.rstrip()) #remove espaço da direita

#Junções e centralização
#exemplo

curso = "Python"

print(curso.center(10, "#"))
print(".".join(curso)) 

#--------------------------------

nome = "MikAeL"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "    Olá Mundo! "
print(texto          + ".")
print(texto.strip()  + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")


menu = "Python"
print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
