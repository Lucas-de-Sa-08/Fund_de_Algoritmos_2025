n = int(input("Quantos números gostaria de inserir? "))

numeros = []

for i in range(n):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("\nNúmeros: ", numeros)
print("\nNúmeros em ordem inversa: ", )
for num in reversed(numeros):
    print(num)
