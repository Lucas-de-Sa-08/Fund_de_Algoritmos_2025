def segundo_maior(lista):
    return sorted(set(lista))[-2]

# Testando com sua lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Segundo maior: ", segundo_maior(lista))  # Saída esperada: 8
