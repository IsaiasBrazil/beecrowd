n1,n2,n3,n4 = map(float,input().split(" "))
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1)/10
print("Media: {:.1f}".format(media))
if media >= 7:
    print("Aluno aprovado.")
elif media >= 5:
    print("Aluno em exame.")
    n5 = float(input())
    print("Nota do exame: {:.1f}".format(n5))
    media = (media+n5)/2
    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(media))
else:
    print("Aluno reprovado.")
