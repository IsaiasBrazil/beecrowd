tesoura = ['papel','lagarto']
papel = ['pedra','Spock']
pedra = ['lagarto','tesoura']
lagarto = ['Spock','papel']
Spock = ['tesoura','pedra']
s = ""
t = int(input())
for i in range(t):
    elem1,elem2 = input().split()
    if elem1 == elem2:
        s = "De novo!"
    elif elem1 in tesoura and elem2 == "tesoura" or\
    elem1 in papel and elem2 == "papel" or\
    elem1 in pedra and elem2 == "pedra" or\
    elem1 in lagarto and elem2 == "lagarto" or\
    elem1 in Spock and elem2 == "Spock":
        s = "Raj trapaceou!"
    else:
        s = "Bazinga!"
    print("Caso #{}: {}".format(i+1,s))
