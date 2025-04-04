def main():
    # Inicializa os contadores
    intervalo_0_25 = 0
    intervalo_26_50 = 0
    intervalo_51_75 = 0
    intervalo_76_100 = 0

    print("Digite números positivos (um número negativo encerra o programa):")
    
    while True:
        numero = int(input("Número: "))

        if numero < 0:
            break  # Sai do loop se o número for negativo

        if 0 <= numero <= 25:
            intervalo_0_25 += 1
        elif 26 <= numero <= 50:
            intervalo_26_50 += 1
        elif 51 <= numero <= 75:
            intervalo_51_75 += 1
        elif 76 <= numero <= 100:
            intervalo_76_100 += 1
        # Números maiores que 100 são ignorados

    # Exibe os resultados
    print("\nQuantidade de números em cada intervalo:")
    print(f"[0-25]: {intervalo_0_25}")
    print(f"[26-50]: {intervalo_26_50}")
    print(f"[51-75]: {intervalo_51_75}")
    print(f"[76-100]: {intervalo_76_100}")

# Executa o programa
main()
