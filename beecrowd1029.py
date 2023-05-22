n = int(input())
cont = 0

def  fibo(x):
    atual = 1
    ant  = 0
    for i in range(x):
        prox = atual+ant
        ant = atual
        atual = prox
    return ant

def  fibo2(x):
    atual = 2
    ant  = 0
    for i in range(1,x):
        prox = atual+ant+2
        ant = atual
        atual = prox
    return ant


def recebe(j):
    global cont
    if j<1:
        return
    else:
        x = int(input())
        fibx = fibo(x)
        y = fibo2(x)
        print("fib({}) = {} calls = {}".format(x,y,fibx))
        cont = 0
        return recebe(j-1)
    return
    
recebe(n)
