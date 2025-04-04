def main():
    # Nomes dos sistemas operacionais
    sistemas = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
    votos = [0] * 6  # Lista para armazenar a contagem de votos

    print("Enquete: Qual o melhor Sistema Operacional para uso em servidores?")
    print("Opções:")
    for i, sistema in enumerate(sistemas, 1):
        print(f"{i}º - {sistema}")

    # Entrada de votos
    while True:
        voto = int(input("Digite o número do sistema escolhido (0 para encerrar): "))

        if voto == 0:
            break  # Encerra a votação
        elif 1 <= voto <= 6:
            votos[voto - 1] += 1  # Incrementa o voto na opção correspondente
        else:
            print("Opção inválida! Digite um número entre 1 e 6.")

    # Calcula o total de votos
    total_votos = sum(votos)

    # Exibe os resultados
    print("\nResultado da enquete:")
    print(f"{'Sistema Operacional':<20} {'Votos':<10} {'%'}")
    print("-" * 40)

    if total_votos > 0:
        for i in range(6):
            percentual = (votos[i] / total_votos) * 100
            print(f"{sistemas[i]:<20} {votos[i]:<10} {percentual:.1f}%")
        
        # Determina o vencedor
        max_votos = max(votos)
        vencedor = sistemas[votos.index(max_votos)]
        print("\nO Sistema Operacional mais votado foi o", vencedor,
              f"com {max_votos} votos, correspondendo a {max_votos / total_votos * 100:.1f}% dos votos.")
    else:
        print("Nenhum voto foi computado.")

# Executa o programa
main()
