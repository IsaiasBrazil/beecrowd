n = int(input())
soma = 0
for i in range(n):
    x,y = map(int,input().split(" "))
    if x > y:
        t = x
        x = y
        y = t
    for k in range(x+1,y):
        temp = k
        if temp % 2 != 0:
            soma += temp
    print(soma)
    soma = 0
         
