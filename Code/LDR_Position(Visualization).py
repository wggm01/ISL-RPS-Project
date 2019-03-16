import matplotlib.pyplot as plt
import matplotlib.animation as animation

import serial

ldr = serial.Serial('/dev/ttyACM0') #Ajustar puerto usado
fig = plt.figure()
ax1=fig.add_subplot(1,1,1)
ax1.set_xlim([0,100])
ax1.set_ylim([0,100])

def animate(i):    
    ldrRaw = ldr.readline()
    ldrSep = ldrRaw.split(",")
    x=float(ldrSep[1])
    y=float(ldrSep[2])
    s=float(ldrSep[0])

    if(s==2): 

        print(s)
    	#ax1.clear()
        ax1.set_xlim([0,100])
        ax1.set_ylim([0,100])
    	ax1.plot(x,y,'ro')
	ax1.set_title('Posicion de Objeto')
	ax1.set_xlabel('Eje x')
	ax1.set_ylabel('Eje y')
	
    if(s==1):
	ax1.clear()
        ax1.set_xlim([0,100])
        ax1.set_ylim([0,100])
	ax1.plot(50,50,'ro')
	ax1.set_title('No hay Objeto')
	ax1.set_xlabel('Eje x')
	ax1.set_ylabel('Eje y')	

    if(s==3):
	ax1.clear()
        ax1.set_xlim([0,100])
        ax1.set_ylim([0,100])
	ax1.plot(50,50,'ro')
	ax1.set_title('Calibrando...')
	ax1.set_xlabel('Eje x')
	ax1.set_ylabel('Eje y')
	
ani = animation.FuncAnimation(fig,animate,interval=100) #Intervalo de ejecucion de funcion animate en ms
plt.show()
