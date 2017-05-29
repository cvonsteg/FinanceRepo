#Import Libraries
import numpy as np
import matplotlib.pyplot as plt

#Required for graphical plotting
fig=plt.figure()

#Defint function
def option (x,p_0,p_r):
	if p_0 < x:
		y = p_r
	elif p_0 > x:
		y = (p_0 - x) + p_r
	return y

#Set variables    
p_0 = int(raw_input("Buy Price in pence: "))
p_r = int(raw_input("Premium paid for option: ")
x = np.arange(0,(int(p)+100),10)  

#Configure graph 
ax=fig.add_subplot(1,1,1)
ax.set_title('Basic option Price Map')
ax.plot(x, option(x,p_0,p_r), 'k-')

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

