# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 16:35:09 2025

@author: p4sim
"""

import lightFunctions as j
import matplotlib.pyplot as plt

data = j.readIntensity("Kayf\Hg_white.jpeg", "Kayf\plot_white.jpeg", "mercury", "white")
data_white = j.readIntensity("Kayf\Fil_white.jpeg", "Kayf\plot_filwhite.jpeg", "filament", "white")
data_red = j.readIntensity("Kayf\Fil_red.jpeg", "Kayf\plot_red.jpeg", "filament", "red")
data_yellow = j.readIntensity("Kayf\Fil_yellow.jpeg", "Kayf\plot_yellow.jpeg", "filament", "yellow")
data_green = j.readIntensity("Kayf\Fil_green.jpeg", "Kayf\plot_green.jpeg", "filament", "green")
data_blue = j.readIntensity("Kayf\Fil_blue.jpeg", "Kayf\plot_blue.jpeg", "filament", "blue")



plt.figure()
plt.title("График интенсивностей света лампы накаливания, отражённого от цветных поверхностей")
plt.xlabel("Относительный номер пикселя: 0 = 400 нм, 600 = 780 нм")
plt.ylabel ("Яркость")

#plt.xlim(400, 1000)
plt.plot(data_white, 'k')
plt.plot(data_red, 'r')
plt.plot(data_yellow, 'y')
plt.plot(data_green, 'g')
plt.plot(data_blue, 'b')

plt.show()