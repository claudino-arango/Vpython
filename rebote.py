from visual import *


scene.weidth=500
scene.heigth=700

scene.ambient=0.5
scene.forward=(1,-0.3,0)


piso=box(box=vector(0,0,0.3),size=vector(2,0.1,4),material=materials.wood,color=color.orange)




muro1=box(pos=vector(0,0.9,2),size=vector(2,2,0.1),material=materials.wood,color=color.orange)


muro2=box(pos=vector(0,0.9,-2),size=vector(2,2,0.1),material=materials.wood,color=color.orange)

muro3=box(pos=vector(1,0.9,0),size=vector(0.1,2,4),material=materials.wood,color=color.orange)




#arrow(pos=vector(0,0,0),axis=(1,0,0),length=2,shaftwidth=0.1,material=materials.unshaded)
#label(text="x",pos=vector(2,0,0),box=False,opacity=0.0,color=color.red)

#arrow(pos=vector(0,0,0),axis=( 0,1,0),length=2,shaftwidth=0.1,material=materials.unshaded)


#label(text="y",pos=vector(0,2,0),box=False,opacity=0.0,color=color.red)

#arrow(pos=vector(0,0,0),axis=(0,0,1),length=2,shaftwidth=0.1,material=materials.unshaded)
#label(text="z",pos=vector(0,0,2),box=False,opacity=0.0,color=color.red,shafwidth=20)



xo=0
yo=1.8
zo=-1.8

esfera=sphere(pos=(xo,yo,zo),radius=0.15,color=color.red)

g=9.8

vox=0.3
voy=0.1
voz=3
t=0.1
signo=1
i=0.1
t1=0.2
signo2=0
while True:
    
    
    rate(9)
    
    
    zo= zo + voz*t*signo
    yo= yo + voy*t - 0.5*g*t*t
    voy= voy - g*t
    
    
    if yo<=0.2:
        voy=voy*-0.9
    if zo>=2:
       signo=-1
    if zo<=-2:
        signo=1
    
    if yo<=0.09:
        a=0
    print yo
    esfera.pos=(xo,yo+0.025832299*t,zo)
    
    
    
