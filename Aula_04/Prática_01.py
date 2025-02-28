preco = float(input("Informe preço do produto: R$"))
codigo = int(input("Informe o código do produto: "))

if codigo == 1:
    procedencia = "Sul"

elif codigo == 2:
    procedencia = "Norte"

elif codigo == 3:
    procedencia = "Leste"

elif codigo == 4:
    procedencia = "Oeste"

elif codigo == 5 or codigo == 6:
    procedencia = "Nordeste"

elif codigo == 7 or codigo == 8 or codigo == 9:
    procedencia = "Sudeste"

elif codigo >= 10 and codigo <= 20:
    procedencia = "Centro-Oeste"

elif codigo >= 25 and codigo <= 30:
    procedencia = "Nordeste"

else:
    procedencia = "Importado"
    print("Preço:", preco, "Procedência:", procedencia)