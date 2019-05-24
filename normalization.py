import os
import matplotlib.pyplot as plt
import datetime
import numpy as np

#Normalization to 0-100

#Light from -1 to 400 lux
dataLight = (np.array(LightData)+1)/401*100
dataLightTime = lightT

#Temperature from 15C to 40C
dataTemperature = (np.array(weatherData_temp) - 15)/25*100
dataWeatherTime = weatherT

#humidity from 10 to 50
dataHumidity = (np.array(weatherData_humidity) - 10)/40*100
#dataHumidityTime = weatherT

#pressure from 95000 to 101000
dataPressure = (np.array(weatherData_pressure) - 95000)/(101000-95000)*100

#audioLevel from 0 to 4
dataAudio = (np.array(audioData_level))*100
dataAudioTime = audioT



