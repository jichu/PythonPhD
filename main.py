from tkinter import *
from tkinter import ttk
import math
import ctypes

import spiderhopfield as sp
import samples as data
import preprocessing as pp


win32 = ctypes.windll.user32

def paintSample(signal,S,X,Y):
      canvas = Canvas(root)
      canvas.config(width=S,height=S)
      canvas.place(x=X,y=Y)
      size = int(S/math.sqrt(len(signal)))
      color=("white","black")
      i=0
      for y in range(int(math.sqrt(len(signal)))):
            for x in range(int(math.sqrt(len(signal)))):
                canvas.create_rectangle((size*x, size*y, size*(x+1),size*(y+1)), fill=color[0 if signal[i]==-1 else signal[i]], tags=('palette', 'palettered'))
                i+=1

winW=win32.GetSystemMetrics(1)-100
winH=winW

root = Tk()
root.title("spider-hop")


debug=0

vzory=data.vzoryTest2
test=data.vzorNoiseTest
          
vzory=pp.dataEEG
test=pp.dataEEGtest[10]

if debug==1:
      vzory=data.vzory
      test=sp.NoiseBipolar(vzory[18],25)

result=sp.SpiderHopfield(vzory,test,1)

#print(sp.Position(vzory,result))

size=100

for i in range(len(vzory)):
      paintSample(vzory[i],size,i*size,0)
paintSample(test,size,0,size)
paintSample(result,size,0,size*2)

root.geometry(str(len(vzory)*size)+"x"+str(size*4))

#paintSample(vzory[0])

root.mainloop()


