t = int(input())
n = []
for i in range(1000):
    n.append(i%t)
for j in range(1000):
    print("N[{}] = {}".format(j,n[j]))
