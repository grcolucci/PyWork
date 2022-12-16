from tkinter import *
import math

signalArray = [0] * 1000
ampSlider = 0
freqSlider = 0


def show_values():

        timeCnt = 0.0
        ampInd = ampSlider.get()
        freqInd = freqSlider.get()
        for x in range(len(signalArray)):
                signalArray[x] = ampInd * math.cos((2*math.pi) * freqInd * timeCnt)
                timeCnt += 0.001        
        print (signalArray)


master = Tk()
ampSlider = Scale(master, from_=0, to=10, tickinterval=0.2, orient=HORIZONTAL)
ampSlider.set(3.6)
ampSlider.pack()
freqSlider = Scale(master, from_=0, to=250, orient=HORIZONTAL)
freqSlider.set(50)
freqSlider.pack()
Button(master, text='Show', command=show_values).pack()

mainloop()



