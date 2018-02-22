import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


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


def writeToFile(x):
    data = open("sampleText.txt","a")
    y = random.randint(1,10)
    data.write("{},{}\n".format(x+1,y))
    data.close()

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
