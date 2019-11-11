"""
created by Ding Lingke A0189238N

11/11/2019
"""

import numpy as np
import matplotlib.pyplot as plt

def ft(expected, t):
    lam = 1 / expected
    return lam * np.exp(- lam * t)

def Ft(expected, t):
    lam = 1 / expected
    return 1 - np.exp( - lam * t)

def pdf_cdf():
    t = np.linspace(0, 20, 10000)
    
    plt.figure()
    plt.xlim([0, 20])
    plt.ylim([0, 1])
    plt.grid(color='black', linestyle='-.', linewidth=0.5)
    pdf_3, =plt.plot(t, ft(3, t))
    cdf_3, =plt.plot(t, Ft(3, t))
    
    pdf_4, =plt.plot(t, ft(4, t))
    cdf_4, =plt.plot(t, Ft(4, t))
    
    pdf_5, =plt.plot(t, ft(5, t))
    cdf_5, =plt.plot(t, Ft(5, t))
    
    plt.legend((pdf_3, cdf_3, pdf_4, cdf_4, pdf_5, cdf_5), ('pdf_3', 'cdf_3', 'pdf_4', 'cdf_4', 'pdf_5', 'cdf_5'))
    
    plt.xlabel('$t$')
    plt.ylabel('$Probability$')
    plt.show()

def probability_beyond_x_years(x):
    print("This is the probability of a component that lasts beyong", x, "years")
    
    print("If the expected lifetime is 3, the probability is", 1 - Ft(3, x))
    print("If the expected lifetime is 4, the probability is", 1 - Ft(4, x))
    print("If the expected lifetime is 5, the probability is", 1 - Ft(5, x))
    
if __name__ == '__main__':
    pdf_cdf()
    x = 5
    probability_beyond_x_years(x)