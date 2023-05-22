x = int(input())
z = int(input())
while z <= x:
    z = int(input())
soma = x
qtd = 1
while soma <= z:
    soma += x + qtd
    qtd += 1
print(qtd)
