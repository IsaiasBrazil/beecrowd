'''2) Faça um programa que preencha uma lista com 10 cores diferentes. Depois permita fazer 
uma pesquisa se uma determinada cor existe armazenada na lista, se existir deve ser 
impresso na tela a cor e em qual posição (índice) esta cor está armazenada. A pesquisa 
deve ser feita até que seja digitado FIM na cor a ser pesquisada na lista.'''

cores = ["amarelo", "verde", "laranja", "rosa","roxo", "azul","cinza","prata","marrom","preto"]
cor =""
while cor != "fim":
	cor = input("Digite a cor ou fim para encerrar: ").lower()
	for i in range(len(cores)):
		if cor == cores[i]:
			print(cor," encontrada na posição ", i)
			break
		if i == len(cores) - 1 and cor != "fim":
			print("Cor não encontrada")