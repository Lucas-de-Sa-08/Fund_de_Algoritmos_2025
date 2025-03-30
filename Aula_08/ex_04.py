numeros = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

soma_pares = 0
for num in numeros

print("\nLista: ", numeros)

#T = [11, 7, 2, 4]
#menor = 999999

#for i in range(len(T)):
#    if T[i] < menor:
#        menor = T[i]

#print(T)
#print("Menor valor: ", menor)
######################################################################
# Criar uma lista com 10 elementos fornecidos pelo usuário
#numeros = []
#for i in range(10):
#    num = int(input(f"Digite o {i+1}o numero: "))
#    numeros.append(num)

# Calcular a soma dos elementos pares
soma_pares = sum(num for num in numeros if num % 2 == 0)

# Calcular a soma dos elementos nos índices pares
#soma_indices_pares = sum(numeros[i] for i in range(0, 10, 2))

# Exibir os resultados
#print(f"Soma dos elementos pares: {soma_pares}")
#print(f"Soma dos elementos nos índices pares: {soma_indices_pares}")
######################################################################
