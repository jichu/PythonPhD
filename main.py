from tkinter import *
from tkinter import ttk
import math
import ctypes

import spiderhopfield as sp
import samples as data

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

vzory=data.vzoryTest2
test=data.vzorNoiseTest
          

if debug==0:
      vzory=data.vzory
      test=sp.NoiseBipolar(vzory[18],25)

result=sp.SpiderHopfield(vzory,test,1)

#print(sp.Position(vzory,result))

paintSample(result)


root.mainloop()


