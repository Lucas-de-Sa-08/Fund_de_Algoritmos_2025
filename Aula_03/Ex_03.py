salário = float(input("Digite o valor do salário atual:"))
if salário < 1800:
    novo_salário = salário * 1.1
    print("O funcionário tem direito a 10% de aumento")
    print("O novo salário ser de R$ %.2f" % novo_salário)
    print("Parabéns pelo novo salário!")