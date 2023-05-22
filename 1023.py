# funcao para truncar numero n com c casas decimais
'''
def truncar(n,c):
    d = int(n * 10**c)/10**c
    return d
'''
def truncar(n,c):
    s = str(n)
    d = s[:s.find('.')+c+1]
    return float(d)

n = int(input())
cont  = 0
while n >0:
    pessoas = 0
    consumos = 0
    # l lista de valores
    l = []
    # c = lista de quocientes
    c = []
    # status 0 para não visitado 1 para visitado
    st = []
    # idx para guardar indices em ordem ascendente não visitados
    idx = []
    for i in range(n):
        l.append(input().split())
        pessoa = int(l[i][0])
        consumo = int(l[i][1])
        c.append(consumo/pessoa)
        pessoas += pessoa
        consumos += consumo
        st.append(0)
    # o = quocientes em ordem ascendente
    o = sorted(c)
    '''
    print(l)
    print(c)
    print(o)
    '''
    s=""
    for elem in o:
        for j in range(n):
            if elem == c[j] and st[j] == 0:
                st[j] = 1
                idx.append(j)
                s += str(l[j][0])+"-"+str(int(int(l[j][1])/int(l[j][0])))+" "
    s = s[:-1]
    cont += 1
    print("Cidade# "+str(cont)+":")
    print(s)
    print("Consumo medio: {:.2f} m3.\n".format(truncar((consumos/pessoas),2)))
    n = int(input())
