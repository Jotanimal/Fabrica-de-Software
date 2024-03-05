# Função sem retorno

def funcao_no_return(a, b):
    (a + b)

nulo = funcao_no_return(3, 5)

print(nulo)

# Função com retorno

def funcao_return(a, b):
    return(a + b)

retorno = funcao_return(10, 4)
print(retorno)

# Loop com While

i = 0

while(i < 9):
    i+= 1
    print(i, "é menor que 10")

# Loop com For
    
soma_numeros = 0

for i in range(5):
    numeros = int(input("Digite 5 números: "))
    soma_numeros += numeros 
   
print(soma_numeros)