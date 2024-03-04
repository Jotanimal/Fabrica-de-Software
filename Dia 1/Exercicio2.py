# Criando função de calcular a média.

def calcula_media(a, b, c, d, e):
    return (a + b + c + d + e) /5

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
n5 = float(input("Digite a quinta nota: "))

media = calcula_media(n1,n2,n3,n4,n5) 

print("Sua média é:", media)