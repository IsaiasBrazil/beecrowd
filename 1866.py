def teste(num):
    status = True
    r = 0
    for i in range(num):
        if status:
            r += 1
            status = not status
        else:
            r -=1
            status = not status
    return r
c = int(input())
for i in range(c):
    print(teste(int(input())))
