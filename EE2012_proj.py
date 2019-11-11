"""
created by Ding Lingke 
Matriculation Number: A0189238N

11/11/2019
"""
import numpy as np
import matplotlib.pyplot as plt

"""
Input: number of years that you expect the electrical component to function

Output: the pdf value of the following equation:
    ft = lamda * e^(-lamda * t) in which lamda = 1 / expected
"""
def ft(expected, t):
    lam = 1 / expected
    return lam * np.exp(- lam * t)

"""
Input: number of years that you expect the electrical component to function

Output: the cdf value of the following equation:
    ft = lamda * e^(-lamda * t) in which lamda = 1 / expected
"""

def Ft(expected, t):
    lam = 1 / expected
    return 1 - np.exp( - lam * t)

"""
Input: None

Output: a graph that contains the probability density function
    and cumulative density function of a continuous function with this pdf: ft = lamda * e^(-lamda * t) 
    in which lamda = 1 / expected years for the electrical component to function
"""
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
"""
Input: Number years that the electrical component will last beyond

Output: the probability of the electrical component that will last beyond the input amount of years for 
    expected number of functional years as 3, 4 and 5
"""

def probability_beyond_x_years(x):
    print("This is the probability of a component that lasts beyong", x, "years")
    
    print("If the expected lifetime is 3, the probability is", 1 - Ft(3, x))
    print("If the expected lifetime is 4, the probability is", 1 - Ft(4, x))
    print("If the expected lifetime is 5, the probability is", 1 - Ft(5, x))
    
    
def inverse_get(expected_year, random_number):
    lam = 1 / expected_year
    return (1 / (-lam)) * np.log(1 - random_number)

def inverse_cdf():
    t = np.linspace(0, 20, 10000)
    array_random_number = np.random.rand(100)
    array_cdf_t = [None]*100
    for i in range (100):
        array_cdf_t[i] = inverse_get(3, array_random_number[i])
        
    plt.plot(t, ft(3, t), label = 'pdf_3')
    plt.hist(array_cdf_t, bins=np.arange(20), density = 1, label = 'histogram')  # arguments are passed to np.histogram
    plt.title("PDF against time")
    plt.legend()
    plt.show()
    
    for i in range (100):
        array_cdf_t[i] = inverse_get(4, array_random_number[i])
    plt.plot(t, ft(4, t), label = 'pdf_4')
    plt.hist(array_cdf_t, bins=np.arange(20), density = 1, label = 'histogram')  # arguments are passed to np.histogram
    plt.title("PDF against time")
    plt.legend()
    plt.show()
    
    for i in range (100):
        array_cdf_t[i] = inverse_get(5, array_random_number[i])
    plt.plot(t, ft(5, t), label = 'pdf_5')
    plt.hist(array_cdf_t, bins=np.arange(20), density = 1, label = 'histogram')  # arguments are passed to np.histogram
    plt.title("PDF against time")
    plt.legend()
    plt.show()

"""
Input: None

Output: Run the above program for at least once
"""
if __name__ == '__main__':
    pdf_cdf()
    x = 5
    probability_beyond_x_years(x)
    inverse_cdf()