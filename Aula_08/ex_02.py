#T = [11, 7, 2, 4]

#menor_valor = min(T)

#print("O menor valor da lista é: ", menor_valor)

T = [11, 7, 2, 4]
menor = 999999

for idx in range(len(T)):
    if T[idx] < menor:
        menor = T[idx]

print(T)
print("Menor valor: ", menor)
