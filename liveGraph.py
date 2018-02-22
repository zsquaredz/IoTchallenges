import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random
import serial

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
y = 0
prev = 0


def animate(i):
    pullData = open("sampleText.txt","r").read()
    dataArray = pullData.split('\n')
    x = int(dataArray[-2].split(',')[0])
    writeToFile(x)
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar,yar)

def readBit():
    global prev
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    rcv = ser.readline()
    cmd = rcv.decode('utf-8').rstrip()
    if cmd.isnumeric():
        prev = int(cmd)
        return prev
    elif ' ' in cmd:
        return prev
    elif '-' in cmd:
        cmd = cmd.replace("-", "", 1)
        if '-' in cmd:
            return prev
        else:
            prev = - int(cmd)
            return prev
    else:
        return prev



def writeToFile(x):
    data = open("sampleText.txt","a")
    y = readBit()
    data.write("{},{}\n".format(x+1,y))
    data.close()
    print('{}, {}'.format(x,y))


ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
data = open('sampleText.txt','w')
data.write('0,0\n')
data.close()
