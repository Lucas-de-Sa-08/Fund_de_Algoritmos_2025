comum = lambda a, b: list(set([x for x in a if x in b]))

# Listas fornecidas
a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Chamando a função
resultado = comum(a, b)

# Exibindo o resultado
print(resultado)
