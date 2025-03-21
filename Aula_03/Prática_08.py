import math

# Função para calcular a área total de um cilindro
def calcular_area_total(raio, altura):
    area_base = math.pi * raio ** 2  # Área da base
    area_lateral = 2 * math.pi * raio * altura  # Área lateral
    area_total = area_base + area_lateral  # Área total
    return area_total

# Função para calcular o número de latas de tinta
def calcular_latas(area_total):
    # Sabemos que 1 litro cobre 3m² e que uma lata tem 5 litros
    litros_necessarios = area_total / 3
    latas_necessarias = math.ceil(litros_necessarios / 5)  # Arredondar para cima

    return latas_necessarias

# Função para calcular o custo com base no número de latas
def calcular_custo(latas_necessarias):
    if latas_necessarias == 1:
        preco_unitario = 50.00
    elif latas_necessarias == 2:
        preco_unitario = 48.00
    elif latas_necessarias == 3:
        preco_unitario = 46.00
    else:
        preco_unitario = 45.00

    custo_total = latas_necessarias * preco_unitario
    return custo_total

# Função principal
def main():
    # Entrada de dados
    raio = float(input("Informe o raio do cilindro (em metros): "))
    altura = float(input("Informe a altura do cilindro (em metros): "))

    # Calcular área total do cilindro
    area_total = calcular_area_total(raio, altura)

    # Calcular número de latas necessárias
    latas_necessarias = calcular_latas(area_total)

    # Calcular custo total
    custo_total = calcular_custo(latas_necessarias)

    # Exibir resultados
    print(f"A área total a ser pintada é: {area_total:.2f} m²")
    print(f"Quantidade de latas necessárias: {latas_necessarias}")
    print(f"Custo total para a pintura: R$ {custo_total:.2f}")

# Chamada da função principal
if __name__ == "__main__":
    main()
