a,b= map(int,input().split(" "))
t = b - a if b>a else b+24-a
print("O JOGO DUROU {} HORA(S)".format(t))
