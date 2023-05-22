entrada = input()
def quadrante(x,y):
    if x > 0 and y > 0:
        print("primeiro")
    elif x > 0 and y < 0:
         print("quarto")
    elif x < 0 and y > 0:
         print("segundo")
    elif x < 0 and y < 0:
         print("terceiro")
x,y = map(int,entrada.split())
while x != 0 and y != 0:
    quadrante(x,y)
    entrada = input()
    x,y = map(int,entrada.split())
    
