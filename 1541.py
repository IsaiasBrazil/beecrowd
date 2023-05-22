import math
n = input()

while not n == "0":
    a,b,c = map(int,n.split())
    result = int(math.sqrt(a * b *100/c))
    print(result)
    n = input()
