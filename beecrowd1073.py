n = int(input())
for i in range(1,n+1):
    if i % 2 == 0:
        m = i**2
        print("{:d}^2 = {:d}".format(i,m))

