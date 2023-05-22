t = int(input())
def mdc(a,b):
    if (b == 0):
        return a
    else:
        return mdc(b,a%b)

for i in range(t):
    li = list(map(int,input().split()))
    f1 = min(li)
    f2 = max(li)
    print(mdc(f1,f2%f1))
