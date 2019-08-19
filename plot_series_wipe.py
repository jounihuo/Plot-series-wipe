import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#plt.style.use("seaborn-darkgrid")

Writer = animation.writers['ffmpeg']
writer = Writer(fps=25, metadata=dict(artist='Jouni Huopana'), bitrate=1800)


#Create some data
n_data = 200

data = np.random.randint(0,n_data,size=(n_data, 3))
a = [0,0,0]
idx = 0
for i in data:
    a+=i
    data[idx,:] = a
    idx += 1  
data = pd.DataFrame(data, columns=list('ABC'))

fig, (ax1, ax2) = plt.subplots(2, 1, sharey=True,figsize=(20,12))

w, h = fig.get_size_inches()*fig.dpi

data_max = data.max().max()

def animate(i):
    #Plot data
    ax1.plot(data)
    ax1.set_title('Q-learn trader')
    ax1.set_ylabel('Stock price [$]')
    ax1.set_xlabel('Time')

    ax2.clear()

    nc = 50
    na = np.linspace(1,0,nc)
    
    ax2.plot([i,i],[0,data_max],'k')
    for k in range(nc):
        ax2.plot([i-0.9*k*(n_data/w),i-0.9*k*(n_data/w)],[0,data_max], color = [5/255,155/255,5/255], alpha = na[k]*0.5)
    
    for k in data.columns:
        ax2.plot(data[k][0:i], 'g')
        ax2.plot(i,data[k][i],'go')
    
    ax2.set_ylabel('Portfolio value [$]')
    ax2.set_xlabel('Time')

    ax2.set_xlim((0,n_data))
    ax2.set_ylim((0,data_max))
    
    ax1.set_facecolor((0.8, 0.8, 0.8))
    ax2.set_facecolor((0.8, 0.8, 0.8))
    ax2.legend(['To win','To lose','Do nothing'], loc=2, facecolor='white', framealpha=0.5)

    #plt.show()



ani = matplotlib.animation.FuncAnimation(fig, animate, frames=n_data, repeat=True)
ani.save('test.mp4', writer=writer)

import os
os.system('smplayer test.mp4 -close-at-end')



