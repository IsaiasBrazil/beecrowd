r = []
soma = 0
while len(r)<3:
    line = input()
    if line == "caw caw":
        r.append(soma)
        soma = 0
    else:
        if line[0]=="*":
            soma += 4
        if line[1]=="*":
            soma += 2
        if line[2]=="*":
            soma += 1
print(r[0])
print(r[1])
print(r[2])
        
