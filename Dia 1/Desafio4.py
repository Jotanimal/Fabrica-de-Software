# Criando a classe Animal

class Animal():
    def __init__(self, nome, raca, cor):
        self.nome = nome
        self.raca = raca
        self.cor = cor

# Definindo as hierarquias da classe Animal (Cachorro e Gato)

class Cachorro(Animal):
    def dados(self):
        print("Seu cachorrro se chama {}. É {}. E é {}.".format(self.nome, self.raca, self.cor)) # Utilizando o str.format
    def som(self):
        print("Woof!!")

class Gato(Animal):
    def dados(self):
        print("Seu gato se chama %s." % self.nome, "É %s." % self.raca, "E é %s." % self.cor) # Utilizando o método de ponteiros de C (%s)
    def som(self):
        print("Meown!!")

tipo_animal = input("Você tem um Cachorro ou Gato? \n")

# Condicional para receber input do usuário

if(tipo_animal == "Cachorro"):
    nome = input("Digite o nome do seu cachorro: ")
    raca = input("Digite a raça do seu cachorro: ")
    cor = input("Digite a cor do seu cachorro: ")
    meu_pet = Cachorro(nome, raca, cor)
elif(tipo_animal == "Gato"):
    nome = input("Digite o nome do seu gato: ")
    raca = input("Digite a raça do seu gato: ")
    cor = input("Digite a cor do seu gato: ")
    meu_pet = Gato(nome, raca, cor)

meu_pet.dados()
meu_pet.som()