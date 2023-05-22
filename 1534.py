try:
    n = int(input())
    while n:        
        um = 0
        dois = n - 1
        for k in range(n):
            for i in range(n):
                if i == dois:
                    print(2,end="")
                elif i == um:
                    print(1,end="")
                else:
                    print(3,end="")
            um += 1
            dois -= 1
            print()
        n = int(input())
        
except:
    pass

