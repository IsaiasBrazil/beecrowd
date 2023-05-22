par = []
impar = []
for i in range(15):
    n = int(input())
    if n % 2 ==0:
        par.append(n)
    else:
        impar.append(n)
    if len(impar)>4:
        for j in range(5):
            print("impar[{}] = {}".format(j,impar[j]))
        impar = []
    if len(par)>4:
        for k in range(5):
            print("par[{}] = {}".format(k,par[k]))
        par = []

for l in range(len(impar)):
    print("impar[{}] = {}".format(l,impar[l]))

for m in range(len(par)):
    print("par[{}] = {}".format(m,par[m]))
