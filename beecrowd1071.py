x = int(input())
y = int(input())
if y < x:
    m = y
    y = x
    x = m
soma = 0
for i in range(x,y-1):
    x += 1
    if x % 2 != 0:
        soma += x
print(soma)
    
