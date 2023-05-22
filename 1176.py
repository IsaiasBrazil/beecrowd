def fib(x):
    if x==0:
        return 0
    elif x<=2:
        return 1
    else:
        return fib(x-1)+fib(x-2)

def fibo(x):
    penult = 1
    antepe = 0
    atual = penult+antepe
    if x==0:
        return 0
    elif x<=2:
        return 1
    else:
        for i in range(x):
            if i>0:
                atual = antepe + penult
                antepe = penult
                penult = atual                
        return atual
            
    
t = int(input())    
for i in range(t):
    x = int(input())
    print("Fib({}) = {}".format(x,fibo(x)))
