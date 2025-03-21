def area(altura,base):
    return (base * altura)/2

while(True):
    b = int(input("Informe a base: "))
    a = int(input("Informe a altura: "))
    print("Área do triâmgulo: ", area(a,b))

    continua = input("Quer calcular a área de mais um triângulo? S / N ")

    if continua != 'S':
        break
