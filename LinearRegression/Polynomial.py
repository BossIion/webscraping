import matplotlib.pyplot as plt
import numpy as np

datapoints = 1000

rng = np.random.default_rng()

x = [x for x in range(1, datapoints)]
y = [rng.normal(loc=5*np.log(x), scale=5.0, size=None) for x in range(1, datapoints)]

mymodel = np.poly1d(np.polyfit(x, y, 4)) # 2 is the degree, just tells it what shape its gonna draw

myline = np.linspace(1, datapoints, 100 * datapoints) # makes the line, 100 datapoints per x coordinate to form line

plt.scatter(x, y)
plt.plot(myline, mymodel(myline), color='red')
plt.show()