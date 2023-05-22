n = int(input())

def mat_quad(n):
    for i in range(n):
        add = 1
        for j in range(n):
            if abs(i-j) < 0:
                res = 1
            else:
                res = abs(i-j)
            print("{:>3}".format(res+1),end="")
            if j < n-1:
                print(" ",end="")
        print()


while(n!=0):
    mat_quad(n)
    print()
    n = int(input())

    
