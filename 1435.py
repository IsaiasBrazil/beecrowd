n=int(input())

def matriz_quadrada(t):
    m=[[0 for x in range (t)] for x in range(t)]
    s=""
    for j in range(t):
        for k in range(j,t-j):
            m[j][k]=j+1
            m[k][j] =j+1
            m[t-j-1][k]=j+1
            m[k][t-j-1]=j+1
        for i in range(t):
            s+= "  "+str(m[j][i]) if m[j][i]<10 else " " +str(m[j][i])
            if i < t-1:
                s+=" "
        s+="\n"
    return s
    
while(n>0):
    print(matriz_quadrada(n))
    n=int(input())
