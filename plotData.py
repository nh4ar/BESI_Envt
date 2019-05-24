import os
import matplotlib.pyplot as plt
import datetime
import numpy as np

plotRange = [-120, 30] #minutes [before, after]
#audioT = np.array(audioTime)
#weatherT = np.array(weatherTime)
#lightT = np.array(LightTime)

#for i in range(1):
#for i in range(len(non_agiTimeStamp)):
#    agiTime = non_agiTimeStamp[i]
for i in range(len(agiTimeStamp)):
    agiTime = agiTimeStamp[i]
    timestampRange = [agiTime+datetime.timedelta(minutes=plotRange[0]), agiTime+datetime.timedelta(minutes=plotRange[1])]
    
    fig = plt.figure()
    
    index = np.where((dataLightTime>timestampRange[0]) & (dataLightTime<timestampRange[1]))
    plt.subplot(5, 1, 1)
    plt.plot(dataLightTime[index], dataLight[index])
    plt.ylabel('Light')
#    plt.xticks([])
#    plt.yticks([])
    plt.axvline(x=agiTime, color='r')
    
    
    index = np.where((dataWeatherTime>timestampRange[0]) & (dataWeatherTime<timestampRange[1]))
    plt.subplot(5, 1, 2)
    plt.plot(dataWeatherTime[index], dataTemperature[index])
    plt.ylabel('Temperature')
#    plt.xticks([])
#    plt.yticks([])
    plt.axvline(x=agiTime, color='r')
    
    plt.subplot(5, 1, 3)
    plt.plot(dataWeatherTime[index], dataHumidity[index])
    plt.ylabel('Humidity')
#    plt.xticks([])
#    plt.yticks([])
    plt.axvline(x=agiTime, color='r')
    
    plt.subplot(5, 1, 4)
    plt.plot(dataWeatherTime[index], dataPressure[index])
    plt.ylabel('Pressure')
#    plt.xticks([])
#    plt.yticks([])
    plt.axvline(x=agiTime, color='r')
    
    index = np.where((dataAudioTime>timestampRange[0]) & (dataAudioTime<timestampRange[1]))
    plt.subplot(5, 1, 5)
    plt.plot(dataAudioTime[index], dataAudio[index])
    plt.ylabel('Audio')
#    plt.yticks([])
    plt.axvline(x=agiTime, color='r')
    
    figure = plt.gcf() # get current figure
    figure.set_size_inches(16, 10)
    plt.show()
#    figName = "nonFigures/nonAgiFigure" + str(i) + ".png"
#    figName = "Figures/AgiFigure" + str(i) + ".png"
    figName = "PainFigures/Figure" + str(i) + ".png"
    plt.savefig(figName, dpi=200)
    plt.close()