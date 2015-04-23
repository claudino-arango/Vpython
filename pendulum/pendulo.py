from visual import *


scene.width=500
scene.height=700


scene.ambient=0.5

X=0.25
Y=0.5
Z=0


piso=box(pos=vector(0,0,0),size=vector(1,0.1,1),material=materials.wood,color=color.orange)
vectorv=box(pos=vector(-0.4,0.5,0),size=vector(0.07,1,0.07))
vectorh=box(pos=vector(-0.1,1,0),size=vector(0.7,0.07,0.07))
cuerda=curve(pos=[(0.25,1,0),(X,Y,Z)],radius=0.004,color=color.red)
esfera=sphere(pos=vector(X,Y,Z),radius=0.1,color=color.blue)
l=0.5
w=2*pi*sqrt(9.8/l)
t=0
while true:
    rate(10)
    teta=90*cos(w*t)
    Z=l*sin(teta*pi/180)
    Y=-l*cos(teta*pi/180)+1
    cuerda.pos[1]=(X,Y,Z)
    esfera.pos=vector(X,Y,Z)
 
    t+=0.007
    #esfera=sphere(pos=vector(X,Y,Z),radius=0.1,color=color.blue)      
    




