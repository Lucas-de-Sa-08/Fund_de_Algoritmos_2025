# Criando uma lista
valores = []

# Laço de repetição para rodar 5x
for i in range(5):
    # Solicito os valores
    valor = input(f"Digite o {i+1}º valor: ")
    # Adicionando o número digitado no final da lista
    valores.append(valor)

# Exibi a lista completa
print("\nLista Completa: ", valores)

# Exibi o primeiro elemento
print("\nPrimeiro elemento: ", valores[0])
# Exibi o segundo elemento
print("Último elemento: ", valores[4])
