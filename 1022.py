n = int(input())
for j in range(n):
    ls = input().split()
    n1,d1,n2,d2 = int(ls[0]),int(ls[2]),int(ls[4]),int(ls[6])
    c1,op,c2 = ls[1],ls[3],ls[5]
    if op == "+":
        e1 = (n1*d2 + n2*d1)
        e2 = (d1*d2)
    elif op == "-":
        e1 = (n1*d2 - n2*d1)
        e2 = (d1*d2)
    elif op == "*":
        e1 = (n1 * n2)
        e2 = (d1 * d2)
    else:
        e1 = (n1 * d2)
        e2 = (n2 * d1)
    m = max(e1,e2)
    print(e1,"/",e2," = ",sep="",end="")
    for i in range(m):
        div = m-i
        if e1 % div == 0 and e2 % div == 0:
            e1 = int(e1/div)
            e2 = int(e2/div)
            break
    print(e1,"/",e2,sep="")
