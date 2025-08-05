#wygenerowanie 1000 losowych wartości z rozkł normalnego  średnia:0, sigma:1. narysuj wykres funkcji gęstości i dystrybuanty
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

dane  = np.random.normal(0,1,1000)
x = np.linspace(-4,4,200)

#funkcja gęstości
plt.plot(x,norm.pdf(x,0,1),label="funkcja gęstości")

#dystrybuanta
plt.plot(x,norm.cdf(x,0,1),label="dystrybuanta(CDF)")
plt.hist(dane,bins=30,density=True,alpha=0.3,color='gray',label="histogram")
plt.legend()
plt.title("Gęstość i dystrybuanta rozkładu normalnego")
plt.show()
