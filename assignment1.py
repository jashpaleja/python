import matplotlib.pyplot as plt
from numpy import sin, pi,linspace
x=linspace(-2*pi,2*pi,100)
y=sin(x)*sin(x)/x
plt.plot(x,y)
plt.show()
