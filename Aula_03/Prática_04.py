salário = int(input("Digite o valor do salário atual:"))

if salário > 1250:
    novo_salário = salário * 1.10
    print("O funcionário tem direito a 10% de aumento")
    print("O novo salário vai ser R$ %.2f" % novo_salário)
    print("Parabéns pelo novo salário!")

if salário < 1250:
    novo_salário = salário * 1.15
    print("O funcionário tem direito a 15% de aumento")
    print("O novo salário vai ser R$ %.2f" % novo_salário)
    print("Parabéns pelo novo salário!")
