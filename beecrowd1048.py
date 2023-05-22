s = float(input())
if s>2000:
    p = 4
elif s>1200:
    p = 7
elif s>800:
    p = 10
elif s>400:
    p = 12
else:
    p = 15
rj = s*p/100
ns = s+rj
print("Novo salario: {:.2f}".format(ns))
print("Reajuste ganho: {:.2f}".format(rj))
print("Em percentual: {:d} %".format(p))
