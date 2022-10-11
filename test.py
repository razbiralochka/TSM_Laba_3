import math as m
import numpy as np
import matplotlib.pyplot as plt
from pid_file import pid_class
from random import uniform

t=0
angle =  m.pi
h = 0.01
omega = 0

k = np.zeros(4)
q = np.zeros(4)


t_list = list()
angle_list = list()

pid = pid_class(h, 0, 20, 0.1, 40)



def f1(t,ang,sp):
    return sp

def f2(t,ang,sp):
    return 0.05*m.sin(ang)-pid.gen_signal(ang)-sp*0.01+uniform(-1, 1)



while t < 5:

    angle_list.append(angle)
    t_list.append(t)
    k[0] = h * f1(t,angle,omega)
    q[0] = h * f2(t,angle,omega)
    k[1] = h * f1(t+h/2,angle+k[0]/2,omega+q[0]/2)
    q[1] = h * f2(t+h/2,angle+k[0]/2,omega+q[0]/2)
    k[2] = h * f1(t+h/2,angle+k[1]/2,omega+q[1]/2)
    q[2] = h * f2(t+h/2,angle+k[1]/2,omega+q[1]/2)
    k[3] = h * f1(t+h,angle+k[2],omega+q[2])
    q[3] = h * f2(t+h,angle+k[2],omega+q[2])
    angle = angle + (k[0]+2*k[1]+2*k[2]+k[3])/6
    omega = omega + (q[0]+2*q[1]+2*q[2]+q[3])/6
    t = t + h

plt.plot(t_list,angle_list)
plt.grid()
plt.show()