x=10
y=20
vx=1
vy=1
c1=20
c2=20
alt=20
lar=80
xr=0
yr=0
xr2=0
yr2=0
hr=20
def setup():
    size(600,400)
    xr=width/2-lar/2
    xr2=width/2-lar/2
def draw():
    global x,y,vx,vy,c1,c2,lar,yr
    yr=height-alt
    background(0,255,50)
    rect(xr,yr,lar,hr)  
    rect(xr2,yr2,lar,hr) 
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
    if xc>=xr and xc<=xr+lar and yc==yr:
        vy*=-1
    if xc>=xr2 and xc<=xr2+lar and yc-c1=ddd=yr2+hr:
        vy*=-1
def keyPressed():
    global xr,xr2
    if keyCode==LEFT and xr>0:
        xr-=15
    if keyCode==RIGHT and xr<width-lar:
        xr+=15
    if key=='a' and xr2>0:
        xr2-=15
    if key=='d' and xr2<width-lar:
        xr2+=15
    
