import math

n1 = int(input("Digite dois números para realizar uma multiplicação simples: "))
n2 = int(input())

def multiplicacao(a, b):
    return(a * b)

resultado_mult = multiplicacao(n1,n2)

print("O resultado da multiplicação é", resultado_mult, "!!")

n3 = float(input("Digite dois números reais para realizar uma divisão simples: "))
n4 = float(input())

def divisao(a, b):
    return(a / b)

resultado_div = divisao(n3,n4)
print("O resultado da divisão é", resultado_div, "!!")