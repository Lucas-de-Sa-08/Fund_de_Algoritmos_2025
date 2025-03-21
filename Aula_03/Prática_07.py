Km = float(input("Informe a distância que você deseja percorrer em Km:"))

if Km <= 200:
    Preço = Km * 0.50
    print("O preço que você vai pagar é: R$")

else:
    Preço = Km * 0.45
    print("O preço que você vai pagar é: R$")
#