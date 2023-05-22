a,b,c,d = map(int,input().split(" "))
if c >a:
    h = c - a
    if d<b:
        h -= 1
        m = d+60-b
    else:
        m = d - b
elif c<a:
    h = c+24-a
    if d<b:
        h -= 1
        m = d+60-b
    else:
        m = d - b
else:
    h = 0
    if d<b:
        h = h+23
        m = d+60-b
    elif d >b:
        m = d - b
    else:
        m = d-b
        h += 24

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h,m))
