import math as m
import numpy as np
import matplotlib.pyplot as plt
from pid_file import pid_class
from random import uniform

t=0
angle = 3*m.pi/180
h = 0.001
omega = 0

k = np.zeros(4)
q = np.zeros(4)

c_kr = 0.1
c_dv =1.5
moment = 0.04


t_list = list()
angle_list = list()

pid = pid_class(h, 0, 500, 10, 300)
#pid = pid_class(h, 0, 5, 10,10)


def f1(t,ang,sp):
    return sp

def f2(t,ang,sp):
    return uniform(-5, 5) - c_kr * sp - c_dv * pid.gen_signal(ang)



while t < 3:

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