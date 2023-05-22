par = posi = neg = impar = 0
for i in range(5):
    n = int(input())
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
    if n > 0:
        posi += 1
    elif n < 0:
        neg += 1
print("{} valores par(es)".format(par))
print("{} valores impar(es)".format(impar))
print("{} valores positivo(s)".format(posi))
print("{} valores negativo(s)".format(neg))

