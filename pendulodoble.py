from visual import *
import numpy as np


scene.weidth=500
scene.height=700

scene.ambient=0.5
scene.forward=(-1,-1,-1)

#arrow(pos=vector(0,0,0),axis=(1,0,0),length=2,shaftwidth=0.1,material=materials.unshaded)
#label(text="x",pos=vector(2,0,0),box=False,opacity=0.0,color=color.red)


#label(text="y",pos=vector(0,2,0),box=False,opacity=0.0,color=color.red)

#arrow(pos=vector(0,0,0),axis=(0,0,1),length=2,shaftwidth=0.1,material=materials.unshaded)
#label(text="z",pos=vector(0,0,2),box=False,opacity=0.0,color=color.red,shafwidth=20)


#armazon
verti=box(pos=vector(0,1,0),size=vector(0.1,2,0.1),material=materials.wood,color=color.orange)
hori=box(pos=vector(0.45,2,0),size=vector(1,0.1,0.1),material=materials.wood,color=color.orange)
piso=box(pos=vector(0,0,0),size=vector(2.5,0.1,2.5),material=materials.wood,color=color.orange)


#un pendulo.
x1=0.95
y1=1.25
z1=0
la=curve(pos=[(0.95,2,0),(x1,y1,z1)],radius=0.009,color=color.red)
esferaa=sphere(pos=(x1,y1,z1),radius=0.1,color=color.blue)


#otro pendulo.
x2=0.95
y2=0.5
z2=0

lb=curve(pos=[(x1,y1,z1),(x2,y2,z2)],radius=0.009)
esferab=sphere(pos=(x2,y2,z2),radius=0.1,color=color.green)


l=0.875
w=2*pi*sqrt(9.8/l)
t=0

 
while True:
#rate(10)
    rate(10)
#Angulo entre "dos pendulos".
    L1=np.array([0.95-x1,2-y1,0-z1])
    L2=np.array([x1-x2,y1-y2,z1-z2])
    D=np.vdot(L1,L2)
    magnitudL1=sqrt(L1[0]**2+L1[1]**2+L1[2]**2)
    magnitudL2=sqrt(L2[0]**2+L2[1]**2+L2[2]**2)
    d=np.arccos(D/(magnitudL1*magnitudL2))
    d=d*180/pi
    
#Ecuaciones pendulo doble.
    teta1=d*cos(w*t)
    teta2=190*cos(w*t)
    z1=l*sin(teta1*pi/180)
    y1=-l*cos(teta1*pi/180)+2.1
    z2=l*sin(teta1*pi/180)+l*sin(teta2*pi/180)
    y2=-l*cos(teta1*pi/180)-l*cos(teta2*pi/180)+2.2

#aplicar coordenadas a cada pendulo:
    la.pos[1]=(x1,y1,z1)
    esferaa.pos=vector(x1,y1,z1)
    lb.pos[0]=(x1,y1,z1)
    lb.pos[1]=(x2,y2,z2)
    esferab.pos=vector(x2,y2,z2)
    t+=0.007

    
