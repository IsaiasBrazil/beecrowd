pos = soma = qt = 0
for i in range(6):
    n = float(input())
    if n > 0:
        pos += 1
        soma += n
        qt += 1
print("{} valores positivos".format(pos))
print("{:.1f}".format(soma/qt if qt>0 else 0))
