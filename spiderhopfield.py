import numpy as np
import random
import time

def NoiseBipolar(vzorIn, rate):
      noise=[]
      for i in range(len(vzorIn)):
            if random.uniform(0,1)<rate/100:
                noise.append(-vzorIn[i])
            else:
                noise.append(vzorIn[i])            
      return noise

def NumberMultiplyList(num,l):
    return [num*x for x in l]

def Position(vzoryIn, classes):
      return [[i for i in range(len(vzoryIn)) if vzoryIn[i]==c] for c in classes]

def CreatePatterns(vzoryIn):
      return [vzoryIn[i:i+2] for i in range(0,len(vzoryIn),2)]

def Learn(vzoryIn):
      vahy=np.transpose(np.array(vzoryIn))@np.array(vzoryIn)
      np.fill_diagonal(vahy,0)
      return vahy.tolist()
          
def LearnNets(pat):
      #start_time = time.time()
      patterns=[Learn(p) for p in pat]
      #print("---LearnNets %s seconds ---" % (time.time() - start_time))
      return patterns

def Test2(vzorIn,weight,it):
      #start_time = time.time()
      test=list(vzorIn)
      testArr=np.array(vzorIn)
      tran=np.transpose(np.array(weight))
      for i in range(len(vzorIn)):
            for j in range(it):  # ???
                y=test[i]+testArr@tran[i]
                test[i]=1 if y>0 else -1
      #print("---Test %s seconds ---" % (time.time() - start_time))
      return test

def Test(vzorIn,weight,it):
    #start_time = time.time()
    test=list(vzorIn)
    testArr=np.array(test)
    tran=np.transpose(np.array(weight))
    for i in range(len(vzorIn)):
        #for j in range(2):  # ???
            y=testArr[i]+testArr@tran[i]
            testArr[i]=1 if y>0 else -1
    #print("---Test %s seconds ---" % (time.time() - start_time))
    return testArr.tolist()


def SpiderHopfield(vzoryIn,testIn,it=1,invert=True):
      start_time = time.time()
      classes=list(vzoryIn)
      while len(classes)>1:
            weights = LearnNets(CreatePatterns(classes))
            classes = [Test(testIn,w,it) for w in weights]
            pozice=Position(vzoryIn,classes)
            if invert:
                  pozice2=Position(pozice,[[]])
                  if pozice2!=[[]]:
                        poziceInvert=[Position(vzoryIn,[NumberMultiplyList(-1,classes[p[0]])]) for p in pozice2]
                        for i in range(len(poziceInvert)):
                            if poziceInvert[i][0]!=[]:
                                classes.append(NumberMultiplyList(-1,classes[pozice2[i][0]]))
                        pozice=[Position(vzoryIn,[c])[0] for c in classes]
                  if Position(pozice,[[]])!=[[]]:
                        del classes[Position(pozice,[[]])[0][0]]
      print("--- %s seconds ---" % (time.time() - start_time))
      return classes[0]

