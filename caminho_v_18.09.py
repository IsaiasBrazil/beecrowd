

#p=[0,1,2,3,4,5,6,7,8]

s =[0,0,0,1,1,2,3,3,4]
t =[1,3,4,2,5,5,4,5,5]
m = [[1,3,4],[2,5],[5],[4,5],[5]]
# resultado esperado para matriz = [[0,3,5],[0,4],[1,6,8],[1,7],[2,8]]

tamanho=len(s)
fim = max(t)
inicio = 0
anterior = -1
matriz=[]
posicao = [[] for x in range(tamanho)]
percorrido =[]
buscado = inicio
encontrado = -1
afechar = 0
processo = 0
idx_anterior = -1
aberto=[True for x in range(tamanho)]

# [0,0,0] 

def falta():
    for i in range(len(matriz)):
        if fim != t[matriz[i][-1]]:
            return True
    if len(matriz)<5:
        return True
    return False

def abre_caminhos(percorrido):
  for j in range(1,len(percorrido)):
    aberto[percorrido[j]] = True

def maior_indice(nproc):
    idxs = []
    for i in range(tamanho):
        if s[i] == nproc:
            idxs.append()
    return max(idxs)


while processo<300:
    for i in range(tamanho):
        if s[i] == buscado and aberto[i]:
            aberto[i] = False
            percorrido.append(i)
    matriz.append(percorrido)
    percorrido = []
    buscado = t[buscado]

    processo +=1       
print(matriz)
