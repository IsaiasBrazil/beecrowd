di = input()
hi,mi,si = map(int,input().split(" : "))
df = input()
hf,mf,sf = map(int,input().split(" : "))
w = int(df.replace("Dia ","")) - int(di.replace("Dia ",""))
x = hf - hi
y = mf - mi
z = sf - si

if z < 0:
    z += 60
    y -= 1
if y < 0:
    y += 60
    x -= 1
if x < 0:
    x += 24
    w -= 1
print("{} dia(s)".format(w))
print("{} hora(s)".format(x))
print("{} minuto(s)".format(y))
print("{} segundo(s)".format(z))
