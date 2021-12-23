#-*- coding:utf-8 -*-
# https://stella47.tistory.com/131
# graph animation
# 3가지 회전 조건

#matplotlib tk
import matplotlib.pyplot as plt
import numpy as np
from drawnow import *
import matplotlib

matplotlib.rcParams['font.family'] ='Malgun Gothic'

angles = []
sines_1 = []
sines_2 = []
cosines = []
tt = []
 
def show_plot():
    #plt.subplot(2,1,1)
    plt.plot(angles, sines_1, 'b', label='Cutting')
    plt.plot(angles, sines_2, 'g', label='Swing')
    plt.plot(angles[1:], tt, 'r', label='Material')
    plt.ylim([-1.2, 1.2])
    plt.legend()
    plt.grid()
    plt.xlabel('회전 [2ㅠ]')
    plt.ylabel('Value')
    plt.rcParams['font.family'] = 'Malgun Gothic'

    #plt.subplot(2,1,2)
    #plt.plot(angles,cosines,label='Cosine')
    
    #plt.ylim([-1.2, 1.2])
    #plt.legend()
    #plt.grid()
    #plt.xlabel('Angles [deg]')
    #plt.ylabel('Value')

idx = 0
k = 5
t = k
flag = 0
for x in np.linspace(0, 50*np.pi, 1000):
    angles = np.append(angles, x)
    sines_1  = np.append(sines_1, np.sin(x))
    sines_2  = np.append(sines_2, abs(np.sin((60/(50*7.5))*x)))
    cosines= np.append(cosines, np.cos(x))

    if idx > 0:
        if sines_1[idx] < 0 and sines_1[idx-1] >= 0:
            flag = 1
        
        if flag > 0:
            tt = np.append(tt, 1)
            t += -1
            if t < 0:
                t = k
                flag = 0
        else:
            tt = np.append(tt, 0)
        drawnow(show_plot)
    idx += 1
        
plt.show()




