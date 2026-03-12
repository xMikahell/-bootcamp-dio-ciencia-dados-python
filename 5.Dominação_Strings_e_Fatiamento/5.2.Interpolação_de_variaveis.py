#Em Python temos 3 formas de interpolar variáveis em strings,
#1ª forma é usando o sinal %
#2ª forma é utilizando o metodo format
#3ª forma é utilizando o f strings

#exemplo 1ª forma: 'Old Style'

nome = "Mikael"
idade = 31
profisão = "Programador junior"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso %s" %(nome, idade, profisão, linguagem))

#exemplo 2ª forma: Format

nome = "Mikael"
idade = 31
profisão = "Programador junior"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso {}".format(nome, idade, profisão, linguagem))


#exemplo 3ª forma: F strings

nome = "Mikael"
idade = 31
profisão = "Programador junior"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profisão} e estou matriculado no curso {linguagem}")

#exemplo: Formatar strings com F-strings

PI = 3.14159

print(f"Valor de PI:{PI:.2f}")

#----------------------------------------

nome = "Mikael"
idade = 31
profisão = "Programador junior"
linguagem = "Python"

dados = {"nome": "Mikael", "idade": 28}

print("Nome: %s idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} idade: {0}".format(idade, nome))
print("Nome: {1} idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} idade: {idade}".format(idade=idade, nome=nome))
print("Nome: {name} idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} idade: {idade}".format(**dados))


print(f"Nome: {nome} idade: {idade}")






