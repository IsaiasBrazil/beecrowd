x = list(map(int,input().split()))
a = x[0]
n = x[-1]
soma = a
for i in range(1,n):
    soma += a+i
print(soma)
