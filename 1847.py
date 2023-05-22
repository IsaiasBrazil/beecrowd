a,b,c = map(int,input().split())
avg = sum([a,c])/len([a,c])
if b==avg and c>a:
    print(":)")
else:
    if b>=avg:
        print(":(")
    else:
        print(":)")
