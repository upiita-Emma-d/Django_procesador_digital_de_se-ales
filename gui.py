import serial
import time 
import collections 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import numpy as np

def getSerialData(self, Samples, serialConnection , lines ,linesValueText , lineLabel):
    value = float(serialConnection.readline().strip() ) ##Lee el sensor
    data.append(value) #Guardar lectura en la ultima posicion de la lista
    lines.set_data(range(Samples),data) # Dibuja nueva linea / Draw new line
    lineValueText.set_text(lineLabel + '= '+  str(round(value,2)) )

serialPort = 'COM3'
baudRate = 9600
try :
    serialConnection = serial.Serial(serialPort,baudRate)
except:
    print('No se pudo jeje')

Samples = 100
data = collections.deque([0]* Samples,maxlen=Samples)
sampleTime = 100

#
xmin = 0
xmax = Samples
ymin = 0
ymax = 6

fig = plt.figure(figsize=(13,6))
ax = plt.axes(xlim = (xmin,xmax), ylim = (ymin , ymax))
plt.title("Real-time Sensor reading")
ax.set_xlabel("Muestras")
ax.set_ylabel('Voltaje')

lineLabel = 'Voltaje'
lines = ax.plot([],[], label = lineLabel)[0]
lineValueText = ax.text(0.85, 0.95,'',transform = ax.transAxes)
anim = animation.FuncAnimation(fig,getSerialData,fargs=(Samples,serialConnection,lines,lineValueText,lineLabel), interval = sampleTime)
plt.show()
alConnection.close()