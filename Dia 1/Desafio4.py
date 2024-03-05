class Animal():
    def __init__(self, nome, raca, cor):
        self.nome = nome
        self.raca = raca
        self.cor = cor

class Cachorro(Animal):
    def dados(self):
        print("Seu cachorrro se chama", self.nome, "é", self.raca, "e é", self.cor)
    def som(self):
        print("Woof!!")

class Gato(Animal):
    def dados(self):
        print("Seu gato se chama", self.nome, "é", self.raca, "e é", self.cor)
    def som(self):
        print("Meown!!")

meu_pet = Cachorro("Pepe", "Vira-Lata", "Preto e Branco")

meu_pet.dados()
meu_pet.som()