import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    x = 0
    y = 0
    xar = []
    yar = []
    resfile = open("tweet_sentiment_result.txt","r").read()
    lines = resfile.split('\n')
    for l in lines[:-1]:
        xy = l.split(',')
        x = xy[0]         
        y = xy[1]    
        xar.append(x)
        yar.append(y)
    ax1.clear()
    ax1.plot(xar,yar, linewidth=2, color='m')
    
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
