o = input().upper()
m=[]
soma = 0
qtd = 0
for i in range(12):
    l = []
    for j in range(12):
        n = float(input())
        l.append(n)
        if j<i and i<6 or i>5 and j<11-i:
            soma+=n
            qtd+=1
if o == "S":
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/qtd))
