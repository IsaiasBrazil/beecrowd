def abre_caminhos(percorrido):
  for j in range(1,len(percorrido)):
    aberto[percorrido[j]] = True

s=[0,0,0,1,1,2,3,3,4]
t=[1,3,4,2,5,5,4,5,5]
tamanho=len(s)
fim = max(t)
aberto=[True for x in range(tamanho)]
matriz=[]
percorrido =[]
anterior = 0
buscado = 0
encontrado = -1
processado = 0
idx = -1
while(True in aberto and processado < tamanho**2):
  for i in range(tamanho):
    if s[encontrado] == buscado:
      abre_caminhos(percorrido)
    if s[i] == buscado and aberto[i]:
      encontrado = i
      print(encontrado)
      aberto[i] = False
  percorrido.append(encontrado)
  buscado = t[encontrado]
  if buscado == fim:
    if not percorrido in matriz:
      matriz.append(percorrido)
      percorrido = []
      buscado = 0
      encontrado = 0
  
  processado +=1
  
#2 adiciona  apos 0
#3 se .count>1 clona percorrido
print(matriz)




