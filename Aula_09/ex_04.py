def jogo_adivinhacao():
    palavra_secreta = "EVAPORAR"
    letras_corretas = ["_"] * len(palavra_secreta)  # Inicializa com "_"
    letras_tentadas = set()  # Armazena letras já tentadas

    print("Jogo da Adivinhação - Descubra a palavra secreta!\n")
    
    while "_" in letras_corretas:  # Continua até completar a palavra
        print(" ".join(letras_corretas))  # Exibe o progresso atual
        letra = input("Adivinhe uma letra: ").upper()

        if letra in letras_tentadas:
            print("Você já tentou essa letra. Tente outra!")
        elif letra in palavra_secreta:
            letras_tentadas.add(letra)  # Armazena a letra usada
            for i, char in enumerate(palavra_secreta):
                if char == letra:
                    letras_corretas[i] = letra  # Atualiza a exibição da palavra
        else:
            letras_tentadas.add(letra)
            print("Incorreta!")

    print(f"\nParabéns! Você descobriu a palavra: {palavra_secreta} 🎉")

# Inicia o jogo
jogo_adivinhacao()
