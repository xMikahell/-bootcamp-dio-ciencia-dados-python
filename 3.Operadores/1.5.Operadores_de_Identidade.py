#São operadores usados para comparar se os dois objetos testados \n
#ocupam a mesma posição na memoria

#exemplo_1:

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso

curso is not nome_curso

saldo is limite

#----------------------
#Exemplo_2

saldo = 1000
limite = 500

print(saldo is limite)
print(saldo is not limite)
