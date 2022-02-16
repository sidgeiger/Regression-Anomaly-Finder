# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

def randomPeak():
    #normál eloszlás 2D Gauss függvénnyel
    #https://en.wikipedia.org/wiki/Gaussian_function
    peak[i][j] = amplitude * np.exp(- ((i - centerX)**2+(j - centerY)**2)/(2*sigma) )

datasetCoords = (5, 512, 512)
rnd = random.randint(100, 200)
# 5 tanító dataset létrehozása 512x512 táblázat formájában (numpy.zeros függvénnyel)
#https://numpy.org/doc/stable/reference/generated/numpy.zeros.html
synteticSpectrumDataset = np.zeros(datasetCoords)
# 5 output dataset a kívánt eredmények tárolására
synteticSpectrumOutput = np.zeros(datasetCoords)

#amplitude, sigma, centerX, centerY a 2Dmenziós Gauss függvény változói, lásd lentebb
for element in synteticSpectrumDataset:
    amplitude = rnd * np.random.random()
    centerX = datasetCoords[1] * np.random.random()
    centerY = datasetCoords[2] * np.random.random()
    sigma = rnd * np.random.random()
   #print(amplitude, centerX, centerY, sigma)
    
    peak = np.zeros((datasetCoords[1], datasetCoords[2]))

for i in range(datasetCoords[1]):
    for j in range(datasetCoords[2]):
        randomPeak()

for element in synteticSpectrumDataset :
    fig = plt.figure(figsize=(7,7))
    plt.imshow(peak[0:,0:], cmap='rainbow')
    plt.colorbar()

element = element + peak

for element in synteticSpectrumDataset :
    fig = plt.figure(figsize=(7,7))
    plt.imshow(element, cmap='rainbow')
    plt.colorbar()
