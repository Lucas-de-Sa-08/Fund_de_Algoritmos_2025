numeros = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("\nNúmeros que são maiores que a soma de seus dois antecessores: ")
for i in range(2, 10):
    if numeros[i] > (numeros[i - 1] + numeros[i - 2]):
        print(numeros[i])
