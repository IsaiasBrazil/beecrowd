i=0
j = [1,2,3]
def formater(number):
    if int(number) == number:
        number = int(number)
    else:
        number = float(str("{:.1f}").format(number))
    return number

while i<=2:
    print("I={} J={}".format(i,j[0]))
    print("I={} J={}".format(i,j[1]))
    print("I={} J={}".format(i,j[2]))
    i = formater(i+0.2)
    j[0] = formater(j[0]+0.2)
    j[1] = formater(j[1]+0.2)
    j[2] = formater(j[2]+0.2)
    
