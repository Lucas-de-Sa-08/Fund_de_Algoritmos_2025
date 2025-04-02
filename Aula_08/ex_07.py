temperaturas = [-10, -8, 0, 1, 2, 5, -2, -4]

menor = temperaturas[0]
maior = temperaturas[0]
soma = 0

for i in temperaturas:
    if i < menor:
        menor = i
    if i > maior:
        maior = i
    soma += i

media = soma / len(temperaturas)


print("\nMenor temperatura: ", menor)
print("\nMaior temperatura: ", maior)
print(f"\nMédia das temperaturas: {media:.2f}")
