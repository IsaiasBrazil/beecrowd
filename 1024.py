n = int(input())
for i in range(n):
    m = input()
    s = ""
    r = ""
    for letter in m:
        if letter.isalpha():
            s += chr(ord(letter)+3)
        else:
            s += letter
    s = s[::-1]
    h = int(len(s)/2)
    h1 = s[h:]
    h2 = ""
    for letter in h1:
        h2 += chr(ord(letter)-1)
    res = s[:h] + h2
    print(res)
    
