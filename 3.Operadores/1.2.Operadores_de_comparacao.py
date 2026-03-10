#booleano

saldo = 450
saque = 200

print(saldo == 200) #igualdade (==)



saldo = 450
saque = 200

print(saldo != 200) #diferença (!=)

#--------------------------------------

#Maior que / Maior igual

saldo = 450
saque = 200

print(saldo > saque)

saldo = 450
saque = 200

print(saldo >= saque)
#---------------------------
#Menor que / menor igual

saldo = 450
saque = 200

print(saldo < saque)

saldo = 450
saque = 200

print(saldo <= saque)
#-----------------------------

#Exemplos de Operadores de comparação

saldo = 200
saque = 200

print(saldo == saque)
print(saldo != saque)
print(saldo > saque)
print(saldo >= saque)
print(saldo < saque)
print(saldo <= saque)


#professor pediu para mexer e fazer mais com o que foi dado

saldo = 300
saque = int(input('Quanto deseja sacar? '))

if saldo >= saque:
    saldo = saldo - saque
    print(f"Saque realizado. Saldo atual: R${saldo}")
else:
    print("Saldo insuficiente")
    







