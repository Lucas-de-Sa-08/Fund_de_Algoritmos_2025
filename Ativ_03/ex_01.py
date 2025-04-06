codigo = int(input("Digite o código do produto:"))
qntd = int(input("Digite a quantidade do produto:"))

if codigo == 1:
    preço = float(qntd * 6.00)

elif codigo == 2:
    preço = float(qntd * 6.50)

elif codigo == 3:
    preço = float(qntd * 5.00)

elif codigo == 4:
    preço = float(qntd * 3.00)

elif codigo == 5:
    preço = float(qntd * 2.00)

print("Total: R$ %.2f" % preço)
