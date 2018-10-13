import numpy as np
import matplotlib.pyplot as plt


def plot_graph():
    title = 'Scores by Members'
    N = 8
    data1 = np.random.randint(0, 100, N)
    data2 = np.random.randint(0, 100, N)
    ind = np.arange(N)
    width = 0.35
    p1 = plt.bar(ind, data1, width, color='#d62728')
    p2 = plt.bar(ind, data2, width, bottom=data1)
    plt.ylabel('Scores')
    plt.xlabel('Individual samples')
    plt.title(title)
    plt.xticks(ind, ('I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8'))
    plt.yticks(np.arange(0, 180, 10))
    plt.legend((p1[0], p2[1]), ('Set1', 'Set2'))
    plt.grid(axis='y')
    #plt.savefig(title+'.svg')
    plt.show()


if __name__ == "__main__":
    plot_graph()
