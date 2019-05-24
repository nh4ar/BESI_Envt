import os
import matplotlib.pyplot as plt
import datetime
import time
import numpy as np


#Read Light
LightTime = []
LightData = []

Folder = "C:/Nutta/Local_Data/BESI-C Data/Deployment_1/Relay_Station10014/Light/"
#Folder = "C:/Nutta/Local_Data/BESI/P3D3 data/test/"
files = os.listdir(Folder)
files.sort()

for names in files:
    filename = Folder+names
    
    #read all data in file
    with open(filename, "r") as rawFile:
        rawData = rawFile.readlines()
        
    timeOnFile = rawData[0]
    try:
        initTime = datetime.datetime.strptime(timeOnFile, '%Y-%m-%d %H:%M:%S.%f\n')
    except:
        initTime = datetime.datetime.strptime(timeOnFile, '%Y-%m-%d %H:%M:%S\n')
    
    for i in range(3,len(rawData)): # line 0 to 2 is the headers
        data = rawData[i].split(',')
        LightData.append(float(data[1]))
        
        mSecTime = float(data[0])
        LightTime.append(initTime+datetime.timedelta(seconds=mSecTime))

################################################################################       
##Read Temperature
#tempTime = []
#tempData = []
#
##Folder = "C:/Nutta/Local_Data/BESI/P3D3 data/Relay_Station10024/Light/"
#Folder = "C:/Nutta/Local_Data/BESI/P3D3 data/test/"
#files = os.listdir(Folder)
#files.sort()
#
#for names in files:
#    filename = Folder+names
#    
#    #read all data in file
#    with open(filename, "r") as rawFile:
#        rawData = rawFile.readlines()
#        
#    timeOnFile = rawData[0]
#    initTime = datetime.datetime.strptime(timeOnFile, '%Y-%m-%d %H:%M:%S.%f\n')
#    
#    for i in range(3,len(rawData)): # line 0 to 2 is the headers
#        data = rawData[i].split(',')
#        tempData.append(float(data[1]))
#        
#        mSecTime = float(data[0])
#        tempTime.append(initTime+datetime.timedelta(seconds=mSecTime))
#
################################################################################
#Read Weather        
weatherTime = []
weatherData_temp = []
weatherData_pressure = []
weatherData_humidity = []

Folder = "C:/Nutta/Local_Data/BESI-C Data/Deployment_1/Relay_Station10014/Weather/"
#Folder = "C:/Nutta/Local_Data/BESI/P3D3 data/test/"
files = os.listdir(Folder)
files.sort()

for names in files:
    filename = Folder+names
    
    #read all data in file
    with open(filename, "r") as rawFile:
        rawData = rawFile.readlines()
        
    timeOnFile = rawData[0]
    try:
        initTime = datetime.datetime.strptime(timeOnFile, '%Y-%m-%d %H:%M:%S.%f\n')
    except:
        initTime = datetime.datetime.strptime(timeOnFile, '%Y-%m-%d %H:%M:%S\n')
    
    for i in range(3,len(rawData)): # line 0 to 2 is the headers
        data = rawData[i].split(',')
        weatherData_temp.append(float(data[1]))
        weatherData_pressure.append(float(data[2]))
        weatherData_humidity.append(float(data[3]))
        
        mSecTime = float(data[0])
        weatherTime.append(initTime+datetime.timedelta(seconds=mSecTime))

        
###############################################################################
#Read Audio   
audioTime = []
audioData = []


Folder = "C:/Nutta/Local_Data/BESI-C Data/Deployment_1/Relay_Station10014/AudioF/"
#Folder = "C:/Nutta/Local_Data/BESI/P3D3 data/test/"
files = os.listdir(Folder)
files.sort()

for names in files:
    filename = Folder+names
    
    #read all data in file
    with open(filename, "r") as rawFile:
        rawData = rawFile.readlines()
        
    timeOnFile = rawData[0]
    initTime = datetime.datetime.strptime(timeOnFile, '%Y-%m-%d_%H-%M-%S\n')
    
    for i in range(3,len(rawData)): # line 0 to 2 is the headers
        data = rawData[i].split(',')
        dataFloat = list(map(float, data[1:35]))
        audioData.append(dataFloat)
        
        mSecTime = float(data[0])
        audioTime.append(initTime+datetime.timedelta(seconds=mSecTime))
        
audioData = np.array(audioData)
audioData_level = audioData[:,1]
#use audioData[:,22]