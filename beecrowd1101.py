m, n = map(int,input().split())
while (m > 0 and n > 0):
    soma = 0
    if m > n:
        t = m
        m = n
        n = t
    for i in range(m,n+1):
        soma += i
        print(i,end=" ")
    print(f"Sum={soma}")
    m, n = map(int,input().split())
