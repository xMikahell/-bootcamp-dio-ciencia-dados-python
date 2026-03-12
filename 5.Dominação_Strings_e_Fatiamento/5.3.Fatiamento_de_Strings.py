#Fatiamento de Strings é um tecnica utilizada para retornar substrings \n
#(partes da string original), informando inicio(start), fim (stop) e passo (step):[start: stop[,step]]

#exemplo:

nome_completo = "Mikael Victor Ferreira Sales"

nome_completo[0]
nome_completo[9]
nome_completo[10:]
nome_completo[10:16]
nome_completo[10:16:2]
nome_completo[:]
nome_completo[::-1]

#String Tripla

nome = "Mikael"
mensagem = f'''
    Olá meu nome é {nome}, 
Eu estou aprendendo Python.
    Essa mensagem tem diferentes recuos.'''

print (mensagem)

print("""
               ========= MENU ============
      
      1 - Depositar
      2 - Sacar
      0 - Sair

      ====================================

        Obrigado por usar nosso sistema!
 """)
