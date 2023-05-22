n = int(input())
t = list( map(int,input().split()))
menor = 21
index = 0
for idx in range(len(t)):
    if t[idx]<menor:
        menor = t[idx]
        index = idx
print(index+1)
