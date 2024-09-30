import datetime
import time

def TimeS ():
    nowTime = datetime.datetime.now()
    time.sleep(4) # to test timer 
    return nowTime

def EndS (): 
    EndTime = datetime.datetime.now()
    return EndTime

def ExecutionTime(nowTime, EndTime):
    exectime = EndTime - nowTime
    
    print (exectime)



startTime = TimeS()
#code here 
EndTimer = EndS()
ExecutionTime(startTime,EndTimer)
