nome = "Lucas"
idade = 17
profissao = "Programador"
linguagem = "Python"
saldo = 45.4357897

dados = {"nome": "Lucas", "idade": 17}

print("Nome: %s idade: %d saldo: %f" % (nome, idade, saldo))
print("Nome: {} idade: {}".format(nome, idade))
print("Nome: {1} idade: {0}".format(idade, nome))
print("Nome: {nome} idade: {idade}".format(idade = idade, nome = nome))
print("Nome: {nome} idade: {idade}".format(**dados))
print(f"Nome: {nome} idade: {idade} saldo: {saldo:10.2f}")

