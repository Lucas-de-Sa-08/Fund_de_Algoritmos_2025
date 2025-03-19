valor_compra = float(input("Digite o valor da compra: "))
parcelas = int(input("Digite a quantidade de parcelas: "))

if parcelas == 1:
    desconto = 0.10
elif parcelas == 2 or parcelas == 3:
    desconto = 0.05
else:
    desconto = 0

if valor_compra > 5000:
    desconto += 0.05

print("Desconto total: ",desconto)
print("Valor final da compra com desconto: ",valor_compra / desconto)
print("Cada parcela será de: ",valor_compra / parcelas)