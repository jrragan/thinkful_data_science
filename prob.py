__author__ = 'rragan'

import collections
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def frequency(data):
    """

    :type data: list
    """
    c = collections.Counter(data)
    # calculate the number of instances in the list
    count_sum = sum(c.values())

    for k,v in c.iteritems():
       print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))

def boxplot(data, filename='boxplot.png'):
    plt.boxplot(data)
    plt.show()
    plt.savefig(filename)

def histogram(data, filename='histogram.png'):
    plt.hist(data, histtype='bar')
    plt.show()
    plt.savefig(filename)

def qqplot(data, filename='qqplot.png'):
    plt.figure()
    graph = stats.probplot(data, dist="norm", plot=plt)
    plt.show()
    plt.savefig(filename)

data = [
    [1, 4, 5, 6, 9, 9, 9],
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9],
    np.random.normal(size=1000),
    np.random.uniform(size=1000)
]

for datum in data:
    frequency(datum)
    boxplot(datum)
    histogram(datum)
    qqplot(datum)