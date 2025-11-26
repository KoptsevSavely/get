# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 16:28:07 2025

@author: p4sim
"""

import lightFunctions as j
import matplotlib.pyplot as plt
import numpy as np

data = j.readIntensity("Hg_white.jpeg", "plot_white.jpeg", "mercury", "white")
data_white = j.readIntensity("Fil_white.jpeg", "plot_filwhite.jpeg", "filament", "white")
data_red = j.readIntensity("Fil_red.jpeg", "plot_red.jpeg", "filament", "red")
data_yellow = j.readIntensity("Fil_yellow.jpeg", "plot_yellow.jpeg", "filament", "yellow")
data_green = j.readIntensity("Fil_green.jpeg", "plot_green.jpeg", "filament", "green")
data_blue = j.readIntensity("Fil_blue.jpeg", "plot_blue.jpeg", "filament", "blue")

pixels = np.arange(len(data_white))  # массив пикселей [0, 1, 2, ..., N-1]
wavelengths = 250 + (950 - 250) * pixels / 600  # линейное преобразование



alb_white = [0]*len(data)
alb_red = [0]*len(data)
alb_yellow = [0]*len(data)
alb_green = [0]*len(data)
alb_blue = [0]*len(data)

for i in range (len(data)):
    alb_white[i] = data_white[i]/data_white[i]
    alb_red[i] = data_red[i]/data_white[i]
    alb_yellow[i] = data_yellow[i]/data_white[i]
    alb_green[i] = data_green[i]/data_white[i]
    alb_blue[i] = data_blue[i]/data_white[i]

plt.figure()
plt.xlim (300, 800)
plt.ylim (0,1.05)

plt.title("График альбедо цветных поверхностей")
plt.xlabel("Длина волны, нм")
plt.ylabel("Альбедо")

plt.plot(wavelengths, alb_white, 'k', label = "white")
plt.plot(wavelengths, alb_red, 'r', label = "red")
plt.plot(wavelengths, alb_yellow, 'y', label = "yellow")
plt.plot(wavelengths, alb_green, 'g', label = "green")
plt.plot(wavelengths, alb_blue, 'b', label = "blue")


plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)
plt.show()