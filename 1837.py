a,b = map(int,input().split())
r = 0
for i in range(abs(b)):
    if (a - i)%b == 0:
        r=i
        break
q = int((a-r)/b)
print(q,r)
        
