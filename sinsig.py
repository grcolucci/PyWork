from tkinter import *
import math
import numpy as np
from plotter import Plotter


signalArray = [0] * 1000
timeArray = [0] * 1000
ampSlider = 0
freqSlider = 0


def show_values():

        timeCnt = 0.0
        ampInd = 3.6 # ampSlider.get()
        freqInd = freqSlider.get()
        for x in range(len(signalArray)):
                timeArray[x] = timeCnt
                signalArray[x] = ampInd * math.cos((2*math.pi) * freqInd * timeCnt)
                timeCnt += 0.001        
        # print (signalArray)

        #x = np.linspace(-np.pi, np.pi, 201)

        to_plot = [{
                "title": "Example 1",
                 "type": "plot",
                "data": [timeArray, signalArray]}]
        
        pl = Plotter(to_plot, figsuptitle="Multi-plot")
        pl.show()



master = Tk()
ampSlider = Scale(master, from_=0.0, to=10.0, length=400, tickinterval=0.02, orient=HORIZONTAL)
ampSlider.set(3.6)
ampSlider.pack()
freqSlider = Scale(master, from_=0, to=250, length=800, tickinterval=10, orient=HORIZONTAL)
freqSlider.set(50)
freqSlider.pack()
Button(master, text='Show', command=show_values).pack()

mainloop()



