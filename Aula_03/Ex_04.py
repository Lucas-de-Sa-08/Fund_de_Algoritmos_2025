n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
n3 = float(input("Digite a terceira nota:"))
n4 = float(input("Digite a quarta nota:"))

média = (n1 + n2 + n3 + n4) / 4
print("Sua média %.2f" % média)

if média > 5:

    print("Você foi aprovado!")
else:
    print("Você foi reprovado!")