import matplotlib.pyplot as plt
import numpy as np


def plot_graph():
    # Subplot figure adjustments
    left = 0.125  # the left side of the subplots of the figure
    right = 0.9  # the right side of the subplots of the figure
    bottom = 0.1  # the bottom of the subplots of the figure
    top = 0.9  # the top of the subplots of the figure
    wspace = 0.3  # the amount of width reserved for blank space between subplots
    hspace = 0.5  # the amount of height reserved for white space between subplots
    plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)
    bins = [10, 30, 40, 80, 100]
    # Titles 1
    data = np.random.randint(low=1, high=100, size=200)
    h, b = np.histogram(data, bins)
    width = 0.7 * (b[1] - b[0])
    center = (b[:-1] + b[1:]) / 2
    a1 = plt.subplot(221)
    a1.set_title("Histogram 1")
    a1.set_xlabel("Bins")
    a1.set_ylabel("Frequency")
    a1.grid()
    a1.bar(center, h, align='center', width=width, color='green')
    # Titles 2
    data = np.random.randint(low=1, high=100, size=200)
    h, b = np.histogram(data, bins)
    width = 0.7 * (b[1] - b[0])
    center = (b[:-1] + b[1:]) / 2
    a2 = plt.subplot(222)
    a2.set_title("Histogram 2")
    a2.set_xlabel("Bins")
    a2.set_ylabel("Frequency")
    a2.grid()
    a2.bar(center, h, align='center', width=width, color='red')
    # Titles 3
    data = np.random.randint(low=1, high=100, size=200)
    h, b = np.histogram(data, bins)
    width = 0.7 * (b[1] - b[0])
    center = (b[:-1] + b[1:]) / 2
    a3 = plt.subplot(223)
    a3.set_title("Histogram 3")
    a3.set_xlabel("Bins")
    a3.set_ylabel("Frequency")
    a3.grid()
    a3.bar(center, h, align='center', width=width, color='blue')
    # Titles 4
    data = np.random.randint(low=1, high=100, size=200)
    h, b = np.histogram(data, bins)
    width = 0.7 * (b[1] - b[0])
    center = (b[:-1] + b[1:]) / 2
    a4 = plt.subplot(224)
    a4.set_title("Histogram 4")
    a4.set_xlabel("Bins")
    a4.set_ylabel("Frequency")
    a4.grid()
    a4.bar(center, h, align='center', width=width, color='purple')
    plt.suptitle("Sub plot of hists")
    plt.show()
    return


if __name__ == "__main__":
    plot_graph()
