l = int(input())
t = input()
m = []
for i in range(12):
    line = []
    for j in range(12):
        numero = float(input())
        line.append(numero)
    m.append(line)
if t.lower()=="s":
    print("{:.1f}".format(sum(m[l])))
else:
    print("{:.1f}".format(sum(m[l])/len(m[l])))
