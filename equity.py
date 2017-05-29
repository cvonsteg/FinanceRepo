#Import Libraries
import numpy as np
import matplotlib.pyplot as plt

#Required for graphical plotting
fig=plt.figure()

#Define function
def equity (x,p):
    y=0+(x-p) # y is profit/loss, x is market price, p is purchase price
    return y

#Set variables    
p = int(raw_input("Buy Price in pence: "))
x = np.arange(0,(int(p)+100),10)

#Configure graph 
ax=fig.add_subplot(111)
ax.set_title('Basic Equity Price Map')
ax.plot(x, equity(x,p), 'k-')

#rearranges axes
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.grid(True)  
plt.xlabel('Market Price')
plt.ylabel('Profit/Loss')
plt.xticks(np.arange(min(x)-10, max(x)+10, 10.0))

#call graph
plt.show()

