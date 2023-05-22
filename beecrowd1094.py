coelhos = sapos = ratos = 0

n = int(input())
for i in range(n):
    t = input().upper()
    qt = int(t[0:t.find(" ")])
    tp = t[t.find(" ")+1:]
    if tp == "C":
        coelhos += qt
    elif tp == "R":
        ratos += qt
    elif tp == "S":
        sapos += qt
total = ratos + sapos + coelhos
print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(coelhos))
print("Total de ratos: {}".format(ratos))
print("Total de sapos: {}".format(sapos))
print("Percentual de coelhos: {:.2f} %".format(coelhos * 100 / total))
print("Percentual de ratos: {:.2f} %".format(ratos * 100 / total))
print("Percentual de sapos: {:.2f} %".format(sapos * 100 / total))
