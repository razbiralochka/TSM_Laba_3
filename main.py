import math as m
import numpy as np
import matplotlib.pyplot as plt
from pid_file import pid_class
from random import uniform

t=0
angle = m.radians(10)
h = 0.001
omega = 0

k = np.zeros(4)
q = np.zeros(4)

c_kr = 0.1
c_dv =1.5
moment = 0.04


t_list = list()
angle_list = list()

pid = pid_class(h, 0, 30, 0.1, 5)
#pid = pid_class(h, 0, 0, 0,0)


vars = np.array([omega, angle])
k = np.zeros((2, 4))

def equs(args):

    omega = args[0]
    angle = args[1]

    d_ang = omega
    d_speed = moment+uniform(-5, 5) - c_kr * omega - c_dv * pid.gen_signal(angle)

    res = np.array([d_speed, d_ang])
    return res



while t < 6:
    t_list.append(t)
    angle_list.append(m.degrees(vars[1]))
    k[:, 0] = equs(vars)
    k[:, 1] = equs(vars + k[:, 0] * h / 2) * 2
    k[:, 2] = equs(vars + k[:, 1] * h / 2) * 2
    k[:, 3] = equs(vars + k[:, 2] * h)

    k *= h / 6
    dvars = np.array([sum(elem) for elem in k])
    vars += dvars
    t += h




plt.plot(t_list, angle_list, color = 'red')
plt.xlabel('Время (с)')
plt.ylabel('Угол по крену (гр.)')
plt.grid()
plt.show()