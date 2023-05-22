from datetime import datetime
antes = datetime.now()

num = 3000
lista_primos= []
def primos(numero):
	cont=0
	for i in range(1,numero+1):
		if numero % i == 0:
			cont += 1
		if i == numero:
			if cont ==2:
				return numero
	return False
				
for i in range(num+1):
	if primos(i):
		lista_primos.append(primos(i))
print(lista_primos)

resto = 0
teste = num
index = 0

while teste > 0:
	if index >= len(lista_primos):
		break
	if teste % lista_primos[index] == 0:
		print(teste,"/",lista_primos[index],"=",end="")
		teste /= lista_primos[index]
		print(teste)
	else:
		index += 1
		
depois = datetime.now()
print ("\n\n",(depois - antes).total_seconds()," segundos")