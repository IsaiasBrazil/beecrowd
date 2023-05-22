a,b,c = map(float,input().split(" "))
if (abs(b - c) < a and a < (b + c)) and (abs(a - c)< b and b < (a + c)) and (abs(a - b) < c and c < (a + b)):
    p = a+b+c
    print("Perimetro = {:.1f}".format(p))
else:
    area = (a+b) * c /2
    print("Area = {:.1f}".format(area))
