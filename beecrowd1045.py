l=list(map(float,input().split(" ")))
l.sort(reverse=True)
a,b,c = l
if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if a*a == b*b + c*c:
        print("TRIANGULO RETANGULO")
    if a*a > b*b + c*c:
        print("TRIANGULO OBTUSANGULO")
    if a*a < b*b + c*c:
        print("TRIANGULO ACUTANGULO")
    if a==b==c:
        print("TRIANGULO EQUILATERO")
    elif (a==b or b == c or a==c):
        print("TRIANGULO ISOSCELES")
