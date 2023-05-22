t =float(input())
n = []
for i in range(100):
    n.append(t)
    t/=2
for j in range(100):
    print("N[{}] = {:.4f}".format(j,n[j]))
