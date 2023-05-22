s = float(input())
def taxes(princ):
    taxa = 0
    if princ > 2500:
        taxa += (princ - 2500)*0.28
        princ = 2500
    if princ > 1000:
        taxa += (princ - 1000)*0.18
        princ = 1000
    if princ > 0:
        taxa += princ * 0.08
        princ = 0
    return taxa

if s > 4500:
    s2 = s - 2000
    final = taxes(s2)
    print("R$ {:.2f}".format(final))
elif s > 3000:
    s2 = s - 2000
    final = taxes(s2)
    print("R$ {:.2f}".format(final))
elif s > 2000:
    s2 = s - 2000
    final = taxes(s2)
    print("R$ {:.2f}".format(final))
else:
    print("Isento")
