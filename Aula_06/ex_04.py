t = int(input("Informe o total de linhas e colunas: "))

for linha in range(t):
    for coluna in range(t):
        if coluna >= linha:
            print(" @ ", end='')
        else:
            print(" # ", end='')
    print()