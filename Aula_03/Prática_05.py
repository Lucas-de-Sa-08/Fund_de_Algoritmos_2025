AnoAtual = int(input("Informe o ano atual:"))
AnoNascimento = int(input("Informe o ano de nascimento:"))
Idade = AnoAtual - AnoNascimento
print("Sua idade é:",Idade)

if Idade >= 18:
    print("Você pode tirar a CNH")

else:
    print("Você ainda não pode tirar a CNH")
#