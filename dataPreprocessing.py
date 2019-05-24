import matplotlib.pyplot as plt
import numpy as np

#def meanfilt (x, k):
#    """Apply a length-k median filter to a 1D array x.
#    Boundaries are extended by repeating endpoints.
#    """
#    # assert k % 2 == 1, "Median filter length must be odd."
#    # assert x.ndim == 1, "Input must be one-dimensional."
#    k2 = (k - 1) // 2
#    y = np.zeros ((len (x), k))
#    y[:,k2] = x
#    for i in range (k2):
#        j = k2 - i
#        y[j:,i] = x[:-j]
#        y[:j,i] = x[0]
#        y[:-j,-(i+1)] = x[j:]
#        y[-j:,-(i+1)] = x[-1]
#    return np.mean (y, axis=1)

def medfilt (x, k):
    """Apply a length-k median filter to a 1D array x.
    Boundaries are extended by repeating endpoints.
    """
    # assert k % 2 == 1, "Median filter length must be odd."
    # assert x.ndim == 1, "Input must be one-dimensional."
    k2 = (k - 1) // 2
    y = np.zeros ((len (x), k))
    y[:,k2] = x
    for i in range (k2):
        j = k2 - i
        y[j:,i] = x[:-j]
        y[:j,i] = x[0]
        y[:-j,-(i+1)] = x[j:]
        y[-j:,-(i+1)] = x[-1]
    return np.median (y, axis=1)

window_len = 3
dataHumidity = medfilt(dataHumidity, 60)
#dataTest = meanfilt(dataTest, 9)

dataPressure = medfilt(dataPressure, 10)
dataTemperature = medfilt(dataTemperature, 10)

#fig = plt.figure()
#plt.plot(dataWeatherTime, dataTemperature)
#plt.plot(dataWeatherTime, dataTest)