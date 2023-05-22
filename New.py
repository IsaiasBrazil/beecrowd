regiao = int(input("Olá,Seja muito bem"\
		"vindo a companhia Tabajara\n" \
		"Selecione a Região: 1-Norte, "\
		"2-Nordeste, 3-Centro-Oeste,"\
		"4-Sul \nDigite a opção \n"))
nome_regiao = ["Norte","Nordeste",\
	"Centro-Oeste", "Sul"]
print("Agora selecione o tipo de"\
	"viagem para o " , nome_regiao[regiao-1],":\n") 
tipo_viagem = input("Selecione o tipo de 	viagem:  ")
if regiao == 1 and tipo_viagem == "1" : print("Valor de Ida é de R$ 500,00") 
elif regiao == 1 and tipo_viagem == "2": print("Valor de Ida e Volta é de R$ 950,00")
else: print("Opção Invalida")