#T = [11, 7, 2, 4]

#menor_valor = min(T)

#print("O menor valor da lista é: ", menor_valor)

T = [11, 7, 2, 4]
menor = 999999

for i in range(len(T)):
    if T[i] < menor:
        menor = T[i]

print(T)
print("Menor valor: ", menor)
