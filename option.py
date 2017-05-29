import numpy as np
import matplotlib.pyplot as plt

## Define Variables ##
S0 = int(raw_input("Agreed execution price (pence): "))
Pm = int(raw_input("Premium paid for option (pence): "))

## Set up empty arrays ##
x = [] ## Market Price
y = [] ## Long Call
a = [] ## Short Call
b = [] ## Long Put
c = [] ## Short Put

## Populate 'Market Price' array ##
for i in range(0, S0+101):
	x.append(i)

## Populate 'Long Call' and 'Short Call' arrays ##
for i in range(0, S0):
	p = -Pm
	q = Pm
	y.append(p)
	a.append(q)
for i in range(S0, S0+101):
	p = -Pm + (x[i]-S0)
	q = -p
	y.append(p)
	a.append(q)
for i in range(0, S0):
    p = (S0-x[i]) - Pm
    q = -p
    b.append(p)
    c.append(q)
for i in range(S0, S0+101):
    p = -Pm
    q = Pm
    b.append(p)
    c.append(q)

## Configure plotting abstraction ##
fig=plt.figure()

## Plot Figures ##
## Plot Call Option ##
ax=fig.add_subplot(211)
ax.plot(y, 'm', label = 'Long Call')
ax.plot(a, 'r', label = 'Short Call')
ax.set_title("Call Option")
plt.xlabel("Price of underlying [GBP]")
plt.ylabel("Profit/Loss [GBP]")
plt.xticks(np.arange(0, max(x)+10, 10))
plt.yticks(np.arange(np.round(-max(x),10), np.round(max(x)+10,10), 20))
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
legend = ax.legend(loc = 'upper right', shadow = True)
plt.grid(True)

## Plot Put Option ##
ax=fig.add_subplot(212)
ax.plot(b, 'k', label = 'Long Put')
ax.plot(c, 'g', label = 'Short Put')
ax.set_title("Put Option")
plt.xlabel("Price of underlying [GBP]")
plt.ylabel("Profit/Loss [GBP]")
plt.xticks(np.arange(0, max(x)+10, 10))
plt.yticks(np.arange(np.round(-max(x),10), np.round(max(x)+10,10), 20))
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
legend = ax.legend(loc = 'upper right', shadow = True)
plt.grid(True)

plt.show()
