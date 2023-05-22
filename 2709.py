def primo(numero):
    if numero == 2 or numero == 3 or numero == 5 or numero == 7:
        return True
    if numero % 2 == 0:
        return False
    if numero % 3 ==0:
        return False
    if numero % 5 ==0:
        return False
    if numero % 7 ==0:
        return False
    if numero <2:
        return False
    return True

soma = 0
try:        
    for m in iter(input,""):
        soma = 0
        m = int(m)
        coins = []
        for i in range(m):
            v = int(input())
            coins.append(v)
        n = int(input())
        for j in range(m-1,0,-n):
            soma += coins[j]
        if primo(soma):
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
        else:
            print("Bad boy! I’ll hit you.")
except:
    pass
