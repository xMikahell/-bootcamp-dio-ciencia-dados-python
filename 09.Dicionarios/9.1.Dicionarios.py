# Um dicionário é um conjunto não-ordenado de pares
#chave:valor, onde as chaves são unicas em uma dada 
#instância do dicionário. Dicionários são delimitados por
#chaves: {}, e contem uma lista de pares chave:valor separada
#por virgulas


#Exemplo

pessoa = {"nome": "Mikael", "idade": 31}

pessoa = dict(nome="Mikael", idade = 31)

pessoa["telefone"] = "*1818181818"

#acesso de dados

dados = {"nome": "Mikael", "idade": 31, "telefone": "8181818181"}

dados["nome"]
dados["idade"]
dados["telefone"]

dados["nome"] = "Gabriela"
dados["idade"] = "30"
dados["telefone"] = "000002002"

dados

#Dicionários aninhados 

#exemplo


contatos = {
    "mikael@gmail.com": {"nome": "Mikael", "telefone": "212312121"},
    "gabriela@gmail.com": {"nome": "Gabriela", "telefone": "0202020202"},
    "joaquim@gmail.com": {"nome": "Joaquim", "telefone": "2122112211"}

}

contatos ["gabriela@gmail.com"]["telefone"]

#iterar

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
        print(chave, valor)


#exemplo dicionari

contatos = {"gabriela@gmail.com": {"nome": "Gabriela", "telefone": "22222222"}}

resultado = contatos.keys()

novo_dicionario = {"a": 100, 1: "teste", "b": "python"}
print(novo_dicionario.keys())


#{}.pop

contatos = {"gabriela@gmail.com": {"nome": "Gabriela", "telefone": "22222222"}}

contatos.pop("gabriela@gmail.com")
contatos.pop("gabriela@gmail.com", {})

#{}.popitem
contatos = {"gabriela@gmail.com": {"nome": "Gabriela", "telefone": "22222222"}}

contatos.popitem()

#{}.setdefault
contato = {"gabriela@gmail.com": {"nome": "Gabriela", "telefone": "22222222"}}

contato.setdefault("nome", "Mikael")
contato

contato = {"gabriela@gmail.com": {"nome": "Gabriela", "telefone": "22222222"}}
contato.setdefault("idade", 28)

#{}.update

contatos = {"gabriela@gmail.com": {"nome": "Gabriela", "telefone": "22222222"}}
contatos

contatos.update({"mikaelv@gmail.com": {"nome": "Mikael", "telefone": "22322222"}})
contatos 

#{}.values

contatos = {"gabriela@gmail.com": {"nome": "Gabriela", "telefone": "22222222"},
            "mikaelv@gmail.com": {"nome": "Mikael", "telefone": "22234445"},
            "joaquimj@gmail.com": {"nome": "Joaquim", "telefone": "22234445"}
}

contatos.values()

#in

contatos = {"gabriela@gmail.com": {"nome": "Gabriela", "telefone": "22222222"},
            "mikaelv@gmail.com": {"nome": "Mikael", "telefone": "22234445"},
            "joaquimj@gmail.com": {"nome": "Joaquim", "telefone": "22234445"}
}

"gabriela@gmail.com" in contatos #True
"megui@gmail.com" in contatos #false
"idade" in contatos["mikaelv@gmail.com"] #false
"telefone" in contatos["joaquimj@gmail.com"] #true 

#del

contatos = {"gabriela@gmail.com": {"nome": "Gabriela", "telefone": "22222222"},
            "mikaelv@gmail.com": {"nome": "Mikael", "telefone": "22234445"},
            "joaquimj@gmail.com": {"nome": "Joaquim", "telefone": "22234445"},
            "chappie@gmail.com": {"nome": "Chappie", "telefone": "11112222"}
}

del contatos["mikaelv@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]