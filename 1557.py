n = int(input())

while n != 0:
        
    t = len(str(2**(n+n-2)))
    s = ""
    for i in range(n):
        for j in range(n):
            s += "{:>"+str(t)+"}"
            s += " " if j < n-1 else ""
            s = s.format(2**i*2**j)
        s += "\n"
    print(s)
    n = int(input())
