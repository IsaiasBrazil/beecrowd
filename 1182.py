c = int(input())
t = input()
m = []
for i in range(12):
    line = []
    for j in range(12):
        numero = float(input())
        line.append(numero)
    m.append(line)

soma = 0
for j in range(12):
    soma += m[j][c]
if t.lower()=="s":
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/12))
