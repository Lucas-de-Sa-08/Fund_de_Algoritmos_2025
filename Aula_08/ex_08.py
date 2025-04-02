# Programa que lê palavras do usuário e exibe sem repetições

palavras = []

while True:
    palavra = input("Digite uma palavra: ").strip()
    if palavra == "":
        break
    if palavra not in palavras:
        palavras.append(palavra)

# Exibir palavras sem repetição na ordem inserida
print("\nPalavras digitadas:")
for palavra in palavras:
    print(palavra)
