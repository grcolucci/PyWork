import matplotlib.pyplot as plt
import numpy as np
import time
import math
from tkinter import *
import (FigureCanvasTkAgg, NavigationToolbar2Tk)

signalArray = [0.0] * 1000
timeArray = [0.0] * 1000
ampSlider = 0
freqSlider = 0
def show_values():
    timeCnt = 0.0
    ampInd = ampSlider.get()
    freqInd = freqSlider.get()
    for x in range(len(signalArray)):
        timeArray[x] = timeCnt
        signalArray[x] = ampInd * math.cos((2*math.pi) * freqInd * timeCnt)
        timeCnt += 0.001


    x = timeArray ## np.arange(0, 1.1, 0.2)
    y = signalArray ##np.sin(x*np.pi)

    fig, ax = plt.subplots(figsize=(3,2), constrained_layout=True)
    ax.plot(x, y)
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Amplitude')
    ax.set_title('Sine wave')
    fig.set_facecolor('lightsteelblue')
    fig.set_size_inches (12,8)
    fig.set

    ## plt.show()
    canvas = FigureCanvasTkAgg(fig,
                               master = window)  
    canvas.draw()


master = Tk()
#Scale(frame, from_=0.55, to=4.75, digits = 3, resolution = 0.01, label = "Lower")
ampSlider = Scale(master, from_=0.00, to=10.2, digits=3, resolution = 0.01, label="Amplitude", length=800, tickinterval=0.02, orient=HORIZONTAL)
ampSlider.set(3.6)
ampSlider.pack()
freqSlider = Scale(master, from_=0, to=250, length=800, tickinterval=10, label="Frequency", orient=HORIZONTAL)
freqSlider.set(50)
freqSlider.pack()
Button(master, text='Show', command=show_values).pack()

mainloop()



