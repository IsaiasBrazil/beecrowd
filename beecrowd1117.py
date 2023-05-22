notasvalidas = 0
media = 0
while notasvalidas < 2:
    s1 = float(input())
    if s1 >= 0 and s1 <= 10:
        media += s1
        notasvalidas += 1
    else:
        print("nota invalida")
    s2 = float(input())
    if s2 >= 0 and s2 <= 10:
        media += s2
        notasvalidas += 1
    else:
        print("nota invalida")
media /= 2
print(f"media = {media:.2f}")
