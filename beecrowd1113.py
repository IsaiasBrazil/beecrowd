x, y = map(int,input().split())
while x != y:
    if x < y:
        print("Crescente")
    else:
        print("Decrescente")
    x, y = map(int,input().split())
