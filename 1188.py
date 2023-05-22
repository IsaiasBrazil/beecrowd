o = input().upper()
m=[]
soma = 0
qtd = 0
for i in range(12):
    l = []
    for j in range(12):
        n = float(input())
        l.append(n)
        if i>6 and (j>11-i and j<i):
            #print(i,j)
            soma+=n
            qtd+=1
if o == "S":
    print(soma)
else:
    print(soma/qtd)
