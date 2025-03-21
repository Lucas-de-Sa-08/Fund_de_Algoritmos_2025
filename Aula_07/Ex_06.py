from math import sqrt

def media(x,y):
    return (x + y) / 2

def calculo(n1,n2,n3):
    return sqrt(n1) + sqrt(n2) + sqrt(n3) + media(n1,n3) + media(n2,n3) + media(n1,n3)

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

print("Resultado do cálculo: ", calculo(a,b,c))
