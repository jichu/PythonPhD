import numpy as np
import loadcsv as data

eeg=np.array(data.EEG)
eegtest=np.array(data.EEGtest)

def Transfer(eeg,channelId=0):
      dataTransfer=[]
      for individual in eeg:
            individualTransfer=[]
            channel=individual[channelId]
            median=np.median(channel)
            ch=[]
            for item in channel:
                  ch.append(1 if item>median else -1)
            dataTransfer.append(ch)
      return dataTransfer

dataEEG=Transfer(eeg)#[:][:16]
dataEEGtest=Transfer(eegtest)#[:][:16]
print(len(dataEEG[0]))
