o = input()
m = []
for i in range(12):
    line = []
    for j in range(12):
        numero = float(input())
        line.append(numero)
    m.append(line)

soma = 0
qtd = 0
idx = 1
for j in range(12):
    for k in range(12):
        if k < (12-idx) and k> idx-1:
            soma += m[j][k]
            qtd +=1
    idx += 1
if o.lower()=="s":
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/qtd))
