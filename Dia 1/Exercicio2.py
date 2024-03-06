# Criando função de calcular a média.

def calcula_media(x):
    return soma_notas /5

soma_notas = 0

# Criando um loop For para o input das notas

for i in range(1, 6):
    notas = float(input("Digite sua nota %d: " % i))
    soma_notas += notas

media = calcula_media(notas) 

print("Sua média é:", media)