n = int(input())
for i in range(n):
    a,b,c = map(float,input().split(" "))
    media = a * .2 + b * .3 + c * .5
    print("{:.1f}".format(media))
