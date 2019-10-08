x=10
y=20
vx=1
vy=1
c1=20
c2=20
alt=20
lar=80
are=30
xc=10
yc=10
def setup():
    size(600,400)
def draw():
    global x,y,vx,vy,c1,c2,lar,bre
    bre=height-alt
    background(0,255,50)
    rect(are,bre,80,20)   
    x+=2*(vx)
    y+=2*(vy)
    ellipse(x,y,c1,c2)
    xc=x
    yc=y+c2/2
    if x>=width or x<0:
        vx*=-1
        ellipse(x,y,c1,c2)
        fill(random(255),random(255),random(255))
    if y>=height or y<=0:
        vy*=-1
        ellipse(x,y,c1,c2)
        fill(random(255),random(255),random(255))
    if xc>=are and xc<=are+lar and yc>=bre:
        vy*=-1
def keyPressed():
    global are
    if keyCode==LEFT and are>0:
        are=are-15
    if keyCode==RIGHT and are<width-lar:
        are=are+15

        
        
        
    
