numeros = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

soma_pares = 0
for num in numeros:
    if num % 2 == 0:
        soma_pares += num

soma_indice_par = 0
for i in range(0, 10, 2):
    soma_indice_par += numeros[i]

print("\nLista: ", numeros)
print("\nSoma dos elementos pares: ", soma_pares)
print("\nSoma dos índices pares: ", soma_indice_par)

# Criar uma lista com 10 elementos fornecidos pelo usuário
#numeros = []
#for i in range(10):
#    num = int(input(f"Digite o {i+1}o numero: "))
#    numeros.append(num)

# Calcular a soma dos elementos pares
#soma_pares = sum(num for num in numeros if num % 2 == 0)

# Calcular a soma dos elementos nos índices pares
#soma_indices_pares = sum(numeros[i] for i in range(0, 10, 2))

# Exibir os resultados
#print(f"Soma dos elementos pares: {soma_pares}")
#print(f"Soma dos elementos nos índices pares: {soma_indices_pares}")
