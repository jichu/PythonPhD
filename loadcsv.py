import csv
import os
import pickle

pathCSV='csv'
pathCache='cachedata.list'
pathCacheTest='cachedata_test.list'

def Transpose(arr):
    return list(map(list, zip(*arr)))

def str2float(s):
    return float(s.replace(',','.'))

def Normalization(data,fv):
    TC=256
    ACdataEEG=[]
    key=0
    for item in data:
        back=str2float(fv[key])
        editedData=[str2float(item[0])-((back*(TC-1)+str2float(item[0]))/TC)]
        for i in range(1,len(item)):
            back=(back*(TC-1)+str2float(item[i]))/TC
            editedData.append(str2float(item[i])-back)  
        ACdataEEG.append(editedData)
        key+=1
    return ACdataEEG

def LoadEEG(file,sampling,trim,offset=0):
    dataEEG=list()
    with open(pathCSV+'/'+file, 'r') as csvfile:            
        reader = csv.reader(csvfile, delimiter=';')
        dataEEG = list(reader)
    channels=dataEEG[0]
    del dataEEG[0] # remove header
    firstValues=dataEEG[0][:14]
    dataEEG=Transpose(dataEEG)
    datatmpEEG=[]
    for i in range(len(dataEEG)-1):
        eachN=dataEEG[i][offset::sampling]
        datatmpEEG.append(eachN[:trim])
    dataEEG=Normalization(datatmpEEG,firstValues)
    #dataEEG=datatmpEEG
    return dataEEG

nameEEG=[]
def DataEEGsamples(sampling,trim,offset=0):
    eeg=list()
    for filename in os.listdir(os.curdir+"/"+pathCSV):
        eeg.append(LoadEEG(filename,sampling,trim,offset))
        nameEEG.append(filename.replace('.csv',''))
        print(filename,'AF3=>',LoadEEG(filename,sampling,trim,offset)[0][:3])
    return eeg

EEG=[]
if os.path.isfile(pathCache)==False:
    with open(pathCache, 'wb') as fp:
        EEG=DataEEGsamples(8,512)
        pickle.dump(EEG, fp)
else:
    with open (pathCache, 'rb') as fp:
        EEG = pickle.load(fp)

EEGtest=[]
if os.path.isfile(pathCacheTest)==False:
    with open(pathCacheTest, 'wb') as fp:
        EEGtest=DataEEGsamples(8,512,512)
        pickle.dump(EEGtest, fp)
else:
    with open (pathCacheTest, 'rb') as fp:
        EEGtest = pickle.load(fp)
