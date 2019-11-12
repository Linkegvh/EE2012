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
    plt.title('PDF and CDF against time')
    plt.legend((pdf_3, cdf_3, pdf_4, cdf_4, pdf_5, cdf_5), ('PDF(t = 3)', 'CDF(t = 3)', 'PDF(t = 4)', 'CDF(t = 4)', 'PDF(t = 4)', 'CDF(t = 5)'))
    
    plt.xlabel('T (number of years)')
    plt.ylabel('Probability')
    plt.show()
"""
Input: Number years that the electrical component will last beyond

Output: the probability of the electrical component that will last beyond the input amount of years for 
    expected number of functional years as 3, 4 and 5
"""

def probability_beyond_x_years(x):
    print("This is the probability of a component that lasts beyond", x, "years")
    
    print("If the expected lifetime is 3 years, the probability is", 1 - Ft(3, x))
    print("If the expected lifetime is 4 years, the probability is", 1 - Ft(4, x))
    print("If the expected lifetime is 5 years, the probability is", 1 - Ft(5, x))
    
"""
Input: The expected functional years and the random number generated from numpy random
    
Output:The inverse CDF result
"""

def inverse_get(expected_year, random_number):
    lam = 1 / expected_year
    return (1 / (-lam)) * np.log(1 - random_number)

"""
Input: no input

Output: print the inverse CDF result on a histogram for expected years as 3, 4 and 5 and their corresponding PDF.
"""
def inverse_cdf_100_points():
    t = np.linspace(0, 20, 10000)
    array_random_number = np.random.rand(100)
    array_cdf_t = [None]*100
    for i in range (100):
        array_cdf_t[i] = inverse_get(3, array_random_number[i])


    plt.plot(t, ft(3, t), label = 'PDF(t = 3)')
    plt.hist(array_cdf_t, bins=np.arange(20), density = 1, label = 'histogram')  
    plt.title("PDF against time 100 data points")
    plt.legend()
    plt.xlabel('T (number of years)')
    plt.ylabel('Probability')
    plt.show()
    
    for i in range (100):
        array_cdf_t[i] = inverse_get(4, array_random_number[i])
    plt.plot(t, ft(4, t), label = 'PDF(t = 4)')
    plt.hist(array_cdf_t, bins=np.arange(20), density = 1, label = 'histogram')  
    plt.title("PDF against time 100 data points")
    plt.legend()
    plt.xlabel('T (number of years)')
    plt.ylabel('Probability')
    plt.show()
    
    for i in range (100):
        array_cdf_t[i] = inverse_get(5, array_random_number[i])
    plt.plot(t, ft(5, t), label = 'PDF(t = 5)')
    plt.hist(array_cdf_t, bins=np.arange(20), density = 1, label = 'histogram')  
    plt.title("PDF against time 100 data points")
    plt.legend()
    plt.xlabel('T (number of years)')
    plt.ylabel('Probability')
    plt.show()

"""
Input: None

Output: Print a graph for 1000 data points inverse transform method histogram
"""
def inverse_cdf_1000_points():
    t = np.linspace(0, 20, 10000)
    array_random_number = np.random.rand(1000)
    array_cdf_t = [None]*1000
    for i in range (1000):
        array_cdf_t[i] = inverse_get(3, array_random_number[i])
    
    array_random_number_1 = np.random.rand(100)
    array_cdf_t_100 = [None]*100
    for i in range (100):
        array_cdf_t_100[i] = inverse_get(3, array_random_number[i])

    plt.subplot(1, 2, 1)
    plt.plot(t, ft(3, t), label = 'PDF(t = 3)')
    plt.hist(array_cdf_t_100, bins=np.arange(20), density = 1, label = 'histogram')  
    plt.title("PDF against time 100 data points")
    plt.legend()
    plt.xlabel('T (number of years)')
    plt.ylabel('Probability')
    #plt.show()


    plt.subplot(1, 2, 2)
    plt.plot(t, ft(3, t), label = 'PDF(t = 3)')
    plt.hist(array_cdf_t, bins=np.arange(20), density = 1, label = 'histogram')  
    plt.title("PDF against time 1000 data points")
    plt.legend()
    plt.xlabel('T (number of years)')
    plt.ylabel('Probability')
    
    plt.tight_layout()
    plt.show()

"""
Input: None

Output: To run the above program for at least once
"""
if __name__ == '__main__':
    pdf_cdf()
    x = 5
    probability_beyond_x_years(x)
    inverse_cdf_100_points()
    inverse_cdf_1000_points()
