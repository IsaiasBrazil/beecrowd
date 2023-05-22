n=int(input())
pum = 1
n *= 4
for  i in range(n):
    if pum % 4 == 0:
        print("PUM")
    else:
        print(pum,end=" ")
    pum += 1
