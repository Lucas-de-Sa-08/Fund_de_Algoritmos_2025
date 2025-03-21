def dataMagica(dia, mes, ano):
    anoUltimos2dig = ano % 100
    multi = dia * mes
    if anoUltimos2dig == multi:
        return True
    else:
        return False

d = int(input("Digite o dia: "))
m = int(input("Digite o mês: "))
a = int(input("Digite o ano: "))

if dataMagica(d, m, a):
    print(f"{d}/{m}/{a} É uma data mágica!")
else:
    print(f"{d}/{m}/{a} Não é uma data mágica!")