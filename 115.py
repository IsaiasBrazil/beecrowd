n=int(input())
while n != 0:
    if n % 2 != 0:
        n += 1
    soma = 0
    for j in range(5):
        soma += n
        n += 2
    print(soma)
    n=int(input())
