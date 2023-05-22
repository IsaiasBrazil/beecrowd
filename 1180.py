n=int(input())
x = list(map(int, input().split()))
menor = x[0]
indice = 0
for idx in range(len(x)):
    if x[idx]< menor:
        menor = x[idx]
        indice = idx
print("Menor valor: {}".format(menor))
print("Posicao: {}".format(indice))

