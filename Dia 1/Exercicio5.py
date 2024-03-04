numero = int(input("Digite um número para saber se é par ou impar: "))

def par_ou_impar():
    if(numero % 2 == 0):
        print("O número digitado é par!!")
    else:
        print("O número digitado é impar!!")

par_ou_impar()