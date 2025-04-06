def media(x, y, z):
    return (x + y + z)/3
    
while(True):
    x = int(input("Informe a primeira nota: "))
    y = int(input("Informe a segunda nota: "))
    z = int(input("Informe a terceira nota: "))
    print("Média aritmética: ", media(x, y, z))
    