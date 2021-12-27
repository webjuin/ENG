#-*- coding:utf-8 -*-
# 인장에 따른 폭 변화 계산

#matplotlib tk
import matplotlib.pyplot as plt
import numpy as np
from drawnow import *
import matplotlib

# 길이 : L
# 폭 : n
# 늘어난 길이 : l
# 좁아진 폭 : x

def show_plot():
    plt.plot(x_1, leng, 'b')
    plt.plot(x_2, leng, 'b')
    
L = 100
n = 10
leng = []
x_1 = []
x_2 = []

for ll in np.linspace(0, 6*n, 100):
    leng = np.append(leng, ll)
    wid_1 = n * ((L/2 - ll) / (L/2 + ll))
    wid_2 = (-1) * n * ((L/2 - ll) / (L/2 + ll))
    x_1 = np.append(x_1, wid_1)
    x_2 = np.append(x_2, wid_2)
    drawnow(show_plot)
plt.show()
