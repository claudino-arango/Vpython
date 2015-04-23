import numpy as np
from visual import *


scene.width=700
scene.height=700

x=-2
y=2
z=0
R=0.2

scene.ambient=0.5
scene.forward=(-3,-1,-3)
esfera=sphere(pos=vector(x,y,z),radius=R,material=materials.earth)
plano=box(pos=vector(1,-0.166,0),size=vector(4.5,0.1,1),material=materials.wood,color=color.orange)
#ejex=box(pos=vector(1,0,0),size=vector(2,0.1,0.1))
#ejey=box(pos=vector(0,1,0),size=vector(0.1,2,0.1))
#ejez=box(pos=vector(0,0,1),size=vector(0.1,0.1,2))
plano.rotate(angle=170*pi/180,axis=(0,0,1),origen=(0,0,1))



t=0.3
teta=10*pi/180
g=9.8
l=1.5
a=y
T=g*sin(teta)*t

while True:
    t=0.2
    y=a+0.1
    i=0
    while y>=-0.2:
        #scene.center=vector(x,y,z)
        rate(15)
        r=g*sin(teta)*t
        alfa=T/(2*pi*R)+t/7
        x=-(l-r)*cos(teta)+(R+(0.1/2))*sin(teta)
        #x=l*cos(teta)-(l-r)*cos(teta)+(R+(0.1/2))*sin(teta)
        y=((l-r)*sin(teta))+(R+(0.1/2))*cos(teta)
        print y
        print "t=",t
        #z=sin(i)
        esfera.pos=vector(x,y,z)
       # rate(9)
        esfera.rotate(angle=-alfa,axis=(0,0,1),origen=(0,0,1))
        t+=0.05
        i+=0.3
        
        

