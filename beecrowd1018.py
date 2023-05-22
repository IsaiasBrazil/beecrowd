N = int(input())
print(N)
h = int(N/100)
N -= h*100
f = int(N/50)
N -= f*50
t = int(N/20)
N -= t*20
d = int(N/10)
N -= d*10
fv = int(N/5)
N -= fv*5
tw = int(N/2)
N -= tw*2
print("{} nota(s) de R$ 100,00".format(h))
print("{} nota(s) de R$ 50,00".format(f))
print("{} nota(s) de R$ 20,00".format(t))
print("{} nota(s) de R$ 10,00".format(d))
print("{} nota(s) de R$ 5,00".format(fv))
print("{} nota(s) de R$ 2,00".format(tw))
print("{} nota(s) de R$ 1,00".format(N))
