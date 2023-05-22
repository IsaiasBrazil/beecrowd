'''1) Escreva um programa que leia a idade de 10 pessoas e armazene-as em uma lista.
Calcule e mostre:
a) a menor idade
b) a média das idades
c) a quantidade de pessoas que tem idade entre 20 e 30 anos (inclusive)
d) a quantidade de pessoas com idade maior que a média
'''
idades = []
entre_idades = maior_media = 0
for i in range(10):
	idade = int(input("Digite a idade: "))
	idades.append(idade)
	if i == 0:
		menor = idade
	if idade < menor:
		menor = idade
	if idade >= 20 and idade <= 30:
		entre_idades += 1
media = sum(idades) / len(idades)
for idade in idades:
	if idade > media:
		maior_media += 1

print("A menor idade: ",menor)
print("A média das idades: ", media)
print(" quantidade de pessoas que tem idade entre 20 e 30 anos (inclusive): ", entre_idades)
print("A quantidade de pessoas com idade maior que a média: ", maior_media)