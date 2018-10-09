#!/usr/bin/python
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import sys
import os.path
import NicksToolbox as NS

#===============================================================================
# EXAMPLE OF LINEAR REGRESSION
#===============================================================================
N = 100      # Number of Observations
F = 2       # Number of Features

x = np.random.random((N,F))
#x = np.linspace(0,10,N)
x = sm.add_constant(x)
beta = np.append(np.array([5]),np.random.random(F)); beta
err = np.random.random(N)
y = np.dot(x,beta) + err

plt.plot(x[:,1],y,'bo', label='Observations')

results = sm.OLS(y, x).fit()
print(results.summary())

if F == 1:
    plt.plot(x[:,1],y,'bo')
    plt.show()

#===============================================================================
#
#===============================================================================
N = 50
x = np.linspace(0,10,N) + 15* np.random.random(N)
y = -3*x + 30 + 10* np.random.random(N)
#plt.rc('text', usetex=True)
NS.ScatterWithHist(x,y)
plt.show()
