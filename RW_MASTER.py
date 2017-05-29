import numpy as np
import matplotlib.pyplot as plt

# Important:  S0 is always defined in y array, therefore y array has tau+1 terms #
#             must account for this when populating x and uniform arrays, either #
#             by setting an initial value or setting range(tau+1)                #



### Define Variables ###
S0 = int(raw_input("Initial stock price in pence: "))
sigma = float(raw_input("Volatility as a %: "))/100
T = int(raw_input("Number of trading days: "))
N = 1440
tau = int(T*N) 

### Setup x and y arrays ###
x = []
y = []

### Array containing random values ###
uniform = []
for i in range(tau+1):
	uniform.append(np.random.uniform(-1,1)) #Sets a random integer which defines whether price change is positive or negative

### Define Stock Price function and append y-array ###
def stock_price(S0, sigma, tau, uniform):
	y.append(S0)
	for i in range(tau):
		Sk = y[i] + (sigma*(tau**0.5))*uniform[i]
		y.append(Sk)

### Populate x array ###
for i in range(tau+1):
	x.append(i+1)

### Call function ###
stock_price(S0,sigma,tau,uniform)

### Plot Graph###
plt.plot(x,y,)
plt.title("Random Walk of Stock Prices")
plt.xlabel("Time (mins)")
plt.ylabel("Price (GBP)")
plt.xticks(np.arange(0, max(x), (60*T)))
plt.xticks(rotation = 75)
plt.grid(True)
plt.show()