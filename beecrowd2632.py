t=int(input())

def colide(raio,center_x,center_y,rect_x,rect_y,rect_w,rect_h):
    x_perto = rect_x
    y_perto = rect_y
    dist_x = abs(center_x - rect_x)
    dist_y = abs(center_y - rect_y)
    for x in range(rect_w+1):
        if abs(rect_x + x  - center_x) < dist_x:
            x_perto = rect_x+x
            dist_x =  abs(rect_x + x  - center_x)
    
    for y in range(rect_h+1):
        if abs(rect_y + y  - center_y) < dist_y:
            y_perto = rect_y+y
            dist_y =  abs(rect_y + y  - center_y)
    distancia = ((center_x-x_perto)**2 +(center_y-y_perto)**2)**0.5
    if  distancia <= raio:
        return True
    else:
        return False
        
for i in range(t):
    w,h,x0,y0 = map(int,input().split())
    s,lv,cx,cy = input().split()
    lv,cx,cy = int(lv),int(cx),int(cy)
    r=0
    if s=="fire":
        pw = 200
        if lv == 1:
            r=20
        elif lv == 2:
            r=30
        elif lv == 3:
            r=50
        
    elif s== "water":
        pw= 300
        if lv == 1:
            r=10
        elif lv == 2:
            r=25
        elif lv == 3:
            r=40       
            
    elif s== "earth":
        pw=400
        if lv == 1:
            r=25
        elif lv == 2:
            r=55
        elif lv == 3:
            r=70
            
    elif s== "air":
        pw=100
        if lv == 1:
            r=18
        elif lv == 2:
            r=38
        elif lv == 3:
            r=60
            
    #colide(raio,center_x,center_y,rect_x,rect_y,rect_w,rect_h):
    if colide(r,cx,cy,x0,y0,w,h):
        print(pw)
    else:
        print(0)
