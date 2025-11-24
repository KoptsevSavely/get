# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 16:35:09 2025

@author: p4sim
"""

import lightFunctions as j
import matplotlib.pyplot as plt
import numpy as np

data = j.readIntensity("Kayf\Hg_white.jpeg", "Kayf\plot_white.jpeg", "mercury", "white")
data_white = j.readIntensity("Kayf\Fil_white.jpeg", "Kayf\plot_filwhite.jpeg", "filament", "white")
data_red = j.readIntensity("Kayf\Fil_red.jpeg", "Kayf\plot_red.jpeg", "filament", "red")
data_yellow = j.readIntensity("Kayf\Fil_yellow.jpeg", "Kayf\plot_yellow.jpeg", "filament", "yellow")
data_green = j.readIntensity("Kayf\Fil_green.jpeg", "Kayf\plot_green.jpeg", "filament", "green")
data_blue = j.readIntensity("Kayf\Fil_blue.jpeg", "Kayf\plot_blue.jpeg", "filament", "blue")


pixels = np.arange(len(data_white))  # массив пикселей [0, 1, 2, ..., N-1]
wavelengths = 250 + (950 - 250) * pixels / 600  # линейное преобразование

plt.figure()
plt.title("График интенсивностей света лампы накаливания, отражённого от цветных поверхностей")
plt.xlabel("Длина волны, нм")
plt.ylabel("Яркость")

# Используем wavelengths вместо pixels
plt.plot(wavelengths, data_white, 'k', label='white')
plt.plot(wavelengths, data_red, 'r', label='red')
plt.plot(wavelengths, data_yellow, 'y', label='yellow')
plt.plot(wavelengths, data_green, 'g', label='green')
plt.plot(wavelengths, data_blue, 'b', label='blue')

plt.xlim(250, 950)  # ограничиваем по длинам волн
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()