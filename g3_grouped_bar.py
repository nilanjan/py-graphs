import numpy as np
import matplotlib.pyplot as plt


def plot_graph():
    family_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    father = np.random.randint(0, 100, 10)
    mother = np.random.randint(0, 100, 10)
    child = np.random.randint(0, 75, 10)
    title = "Family age chart by members"
    plt.figure(1)
    plt.title(title+" Fathers")
    plt.xlabel("Fathers from different families")
    plt.ylabel("Age")
    plt.bar(np.arange(len(father)), father)
    plt.xticks([r for r in range(len(father))], family_name)
    plt.show()

    plt.figure(2)
    plt.title(title+" Mothers")
    plt.xlabel("Mothers from different families")
    plt.ylabel("Age")
    plt.bar(np.arange(len(mother)), mother)
    plt.xticks([r for r in range(len(father))], family_name)
    plt.show()

    plt.figure(3)
    plt.title(title+" Children")
    plt.xlabel("Children from different families")
    plt.ylabel("Age")
    plt.bar(np.arange(len(child)), child)
    plt.xticks([r for r in range(len(father))], family_name)
    plt.show()

    plt.figure(4)
    plt.title(title)
    plt.xlabel("Members")
    plt.ylabel("Age")
    width = 0.25
    r1 = np.arange(len(father))
    r2 = [x + width for x in r1]
    r3 = [x + width for x in r2]
    plt.bar(r1, father, width, label='Father')
    plt.bar(r2, mother, width, label='Mother')
    plt.bar(r3, child, width, label='Child')
    plt.xticks([r + width for r in range(len(father))], family_name)

    plt.show()
    return


if __name__ == "__main__":
    plot_graph()
