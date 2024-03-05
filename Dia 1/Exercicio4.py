# Programa que calcula a maioridade de um usuário

idade = int(input("Digite sua idade: "))

def maior_de_idade():
    if(idade >= 18):
        print("Você é maior de idade!!")
    else:
        print("Você não é maior de idade!!")

maior_de_idade()