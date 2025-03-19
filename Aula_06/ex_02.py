L = int(input("Digite o número de linhas: "))
C = int(input("Digite o número de colunas: "))

def imprimir_bordas(L, C):
    if L <= 0 or C <= 0:
        print("Os valores de L e C devem ser maiores que 0.")
        return
    print('*' * C)
    
    for i in range(L - 2):
        print('*' + ' ' * (C - 2) + '*')
    
    if L > 1:
        print('*' * C)

imprimir_bordas(L, C)
