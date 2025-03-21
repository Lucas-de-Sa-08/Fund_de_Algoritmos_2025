def dataMagica(dia, mes, ano):
    anoUltimos2dig = ano % 100
    multi = dia * mes
    if anoUltimos2dig == multi:
        return True
    else:
        return False
    
for a in range(1901, 2001):
    for m in range(1, 13):
        for d in range(1, 32):
            if dataMagica(d,m,a):
                print(f"{d}/{m}/{a} é uma data mágica!")
