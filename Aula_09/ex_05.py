def count_unique_elements(lista):
    return sum(1 for x in set(lista) if lista.count(x) == 1)

# Teste da função
entrada = [1, 2, 2, 3, 4, 4, 5]
saida = count_unique_elements(entrada)
print(saida)  # Saída esperada: 3
