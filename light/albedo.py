# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 16:28:07 2025

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


alb_red = [0]*len(data)
alb_yellow = [0]*len(data)
alb_green = [0]*len(data)
alb_blue = [0]*len(data)

for i in range (len(data)):
    alb_red[i] = data_red[i]/data_white[i]
    alb_yellow[i] = data_yellow[i]/data_white[i]
    alb_green[i] = data_green[i]/data_white[i]
    alb_blue[i] = data_blue[i]/data_white[i]

plt.figure()
#plt.xlim(400, 1000)
#plt.plot(alb_white, 'k')
plt.plot(alb_red, 'r')
plt.plot(alb_yellow, 'y')
plt.plot(alb_green, 'g')
plt.plot(alb_blue, 'b')

plt.show()