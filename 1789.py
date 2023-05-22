try:
    l = int(input())
    r = 0
    while True:
        v = list(map(int,input().split()))
        s = max(v)
        if s<10:
            r  = 1
        elif s <20:
            r = 2
        else:
            r = 3
        print(r)
        l = int(input())
except:
    pass
            
            
