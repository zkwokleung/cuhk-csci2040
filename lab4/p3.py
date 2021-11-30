# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import numpy as np
def ex3():
    np.random.seed(0)
    mu = 0
    sigma = 1
    random_numbers = mu + sigma*np.random.randn(10000)
    num_bins = 100
    n, bins, patches = plt.hist(random_numbers, num_bins,
                                density=1,
                                color='green')
    x = bins
    y = np.exp((-np.power(x-mu, 2)/np.power(2*sigma, 2))/(sigma*np.sqrt(2*np.pi)))

    #Q1
    plt.plot(x, y, color = 'red',
                linestyle = 'dashed')
    plt.savefig('histogram_line.png', dpi=100)
    plt.show()

    Colleges = {'New Asia College': 3345, 'United College': 3364,
                'Shaw College': 3342, 'Morningside College': 300}
    names = []
    ppls = []
    for x, y in Colleges.items():
        names.append(x)
        ppls.append(y)
    explode = (0, 0, 0, 0.1)

    #Q2
    plt2.pie(ppls, explode=explode, labels=names,
            autopct='%1.1f%%', startangle=0,
            wedgeprops={"edgecolor": "black",
                        'linewidth': 2,
                        'antialiased': True})
    plt2.savefig('pie.png', dpi = 100)
    plt2.show()

    #Q3
    plt3.bar(names, ppls, color ='maroon',
        width = 0.4)

    plt3.savefig('bar.png', dpi=100)
    plt3.show()


if __name__ == '__main__':
    ex3()
