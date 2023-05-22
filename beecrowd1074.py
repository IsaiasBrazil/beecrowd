n = int(input())
for i in range(n):
    s = int(input())
    if s > 0:
        if s % 2 == 0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    elif s < 0:
        if s % 2 == 0:
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
    else:
        print("NULL")
