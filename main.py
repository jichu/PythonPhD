from tkinter import *
from tkinter import ttk
import math
import spiderhopfield as sp
import ctypes
import pprint
import samples

import time

win32 = ctypes.windll.user32

def paintSample(signal):
      size = int(canvasW/math.sqrt(len(signal)))
      color=("white","black")
      i=0
      for y in range(int(math.sqrt(len(signal)))):
            for x in range(int(math.sqrt(len(signal)))):
                canvas.create_rectangle((size*x, size*y, size*(x+1),size*(y+1)), fill=color[0 if signal[i]==-1 else signal[i]], tags=('palette', 'palettered'))
                i+=1

canvasW=win32.GetSystemMetrics(1)-100
canvasH=canvasW
pad=0

root = Tk()
root.title("spider-hop")
root.geometry(str(canvasW)+"x"+str(canvasH))


canvas = Canvas(root)
canvas.config(width=canvasW,height=canvasH)
canvas.place(x=pad,y=pad)

debug=0

vzory=samples.vzoryTest2
test=samples.vzorNoiseTest
          

if debug==0:
      vzory=samples.vzory
      test=sp.NoiseBipolar(vzory[1],10)

result=sp.SpiderHopfield(vzory,test,1)

#print(result)

paintSample(result)


root.mainloop()


