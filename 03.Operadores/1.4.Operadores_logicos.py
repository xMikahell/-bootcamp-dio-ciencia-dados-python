#operadores logicos 

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print (False or False)

saldo = 1000
saque = 200
limite = 100

saldo >= saque 

saque <= limite

#-----------------------
#Operador E(and)
saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite 

#se o conteudo comparado for verdadeiro o resultado é verdadeiro, MAS, se houver uma comparação falsa o resultado é falso, exemplo acima.

#Operador OR (ou):

saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite #

#se o conteudo comparado houver um verdadeiro mesmo com outro dado sendo falso o resultado é verdadeiro, e para retornar falso os conteudos comparados devem ser falsos
#basicamente OR é o contrario de AND

#Operador de Negação

not 1000 > 1500

#O operador de negação (not) serve para inverter uma condição, tive que pedir ajuda a uma IA pq a explicação não foi tão boa
# Ou seja:
# True (verdadeiro) vira False (falso)
# False (falso) vira True (verdadeiro)

#parêntese  

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

saldo_suficiente_conta_normal = (saldo >= saque and saque <= limite) 
saldo_suficiente_conta_especial = (conta_especial and saldo >= saque)

exp_3 = saldo_suficiente_conta_normal or saldo_suficiente_conta_especial
print(exp_3)




