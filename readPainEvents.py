import os
import matplotlib.pyplot as plt
import datetime
import numpy as np

#Folder = "C:/Nutta/Local_Data/BESI/P3D3 data/Relay_Station10024/AudioF/"
#filename = "C:/Nutta/Local_Data/BESI/P3D3 data/agitationTime_Bedroom_EST.txt"
#filename = "C:/Nutta/Local_Data/BESI/P3D3 data/non_agitationTimeP3D3.txt"
filename = "C:/Nutta/Local_Data/BESI-C Data/Deployment_1/painEvents.txt"
with open(filename, "r") as rawFile:
    rawData = rawFile.readlines()
    
agiTimeStamp = []
#non_agiTimeStamp = []
for data in rawData:
    try:
        agiTimeStamp.append(datetime.datetime.strptime(data, '%Y/%m/%d %H:%M:%S\n'))
#        non_agiTimeStamp.append(datetime.datetime.strptime(data, '%Y-%m-%d %H:%M:%S\n'))
    except:
        agiTimeStamp.append(datetime.datetime.strptime(data, '%Y/%m/%d %H:%M:%S'))
#        non_agiTimeStamp.append(datetime.datetime.strptime(data, '%Y-%m-%d %H:%M:%S'))
        
