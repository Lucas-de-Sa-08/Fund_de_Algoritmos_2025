n = int(input("Digite a dimenssão dos vetores: "))

vetor1 = []
print("Digite o vetor 1")
for _ in range(n):
    vetor1.append(int(input()))

vetor2 = []
print("Digite o vetor 2")
for _ in range(n):
    vetor2.append(int(input()))

produto_escalar = sum(vetor1 * vetor2 for vetor1, vetor2 in zip)
print(produto_escalar)
