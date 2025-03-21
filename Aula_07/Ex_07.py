def podeDoar(genero, peso):
    if (genero == "F" and peso >=50) or (genero == "M" and peso >=60):
        return True
    else:
        return False

g = str(input("Informe seu gênero: H se for homem, M se for mulher. "))
p = int(input("Informe seu peso: "))

if podeDoar(g, p):
    print("Pode doar sangue!")
else:
    print("Não pode doar sangue!")