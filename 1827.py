try:
    n = int(input())
    r = 0
    while True:
        dois = 0
        tres = n-1
        quatro = 4
        terco = int(n/3)
        metade = int(n/2)
        s = ""
        for i in range(n):
            for j in range(n):
                if j== metade and i == metade:
                    s += "4"
                elif j >= terco and j < n-terco and i>=terco and i< n-terco:
                    s += "1"
                elif dois == j:
                    s += "2"
                elif tres == j:
                    s+= "3"
                else:
                    s += "0"
            dois += 1
            tres -= 1
            s += "\n"
        print(s)
        n = int(input())
        
except:
    pass
            
            
