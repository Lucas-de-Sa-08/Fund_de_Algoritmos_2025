qntd = int(input("Digite a quantidade de números a serem testados: "))
cont_primos = 0

for i in range(0, qntd):
    numero = int(input(f"Digite o número {i}: "))
    if numero > 1:
        é_primo = True
        for j in range(2,numero):
            if numero % j == 0:
                é_primo + False
                break
        if é_primo:
                cont_primos = cont_primos + 1

print("Total de números: ", qntd)
print("Total de primos: ", cont_primos)