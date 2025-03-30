numeros = []
maior = -999999

for indice in range(10):
    num = int(input(f"Digite o {indice+1}º número real: "))
    numeros.append(num)
    if numeros[indice] > maior:
        maior = numeros[indice]
        indice_maior = indice

print("\nLista: ", numeros)
print("\nMaior valor: ", maior)
print("\nÍndice maior: ", indice_maior)
