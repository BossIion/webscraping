import matplotlib.pyplot as plt
import numpy as np
import random as r
import scipy

datapoints = 25
theoryM = 1.5
theoryB = 19

randUpper = 100
randLower = -100

rng = np.random.default_rng()

x = [x for x in range(datapoints)] #for loop that makes x = 1,2,3,4,5,
y = [rng.normal(loc=theoryM * x + theoryB, scale=10.0, size=None) for x in range(datapoints)] # doesthe same thing as the other loop, mirror, except random placement w the lo of the slope

linRegression = scipy.stats.linregress(x, y)

m = linRegression.slope
b = linRegression.intercept

print(f"y = {m}x + {b}")

def predict(x):
    return m * x + b

plt.scatter(x, y)
plt.plot(x, list(map(predict, x)), color='red')
plt.show()