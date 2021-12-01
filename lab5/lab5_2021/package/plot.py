import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random
from sortTime import selectSort
import myModule


# The array size
arr_size = 10000

# Two excatly same list for 2 sorting method
lst4python = [random.randint(-1000000, 1000000) for _ in range(arr_size)]
lst4C = lst4python.copy()
x = np.arange(0, arr_size)
running = False

# The plot
fig, ax = plt.subplots(nrows=2)
ax[0].scatter(x, lst4python, s=2, c="red")

# Python
ax[0].set_title("Sort using Python")
ax[0].get_xaxis().set_visible(False)

# C
ax[1].set_title("Sort using C")
ax[1].scatter(x, lst4C, s=2, c="blue")

# Animation function


def init():
    ax.set_xlim(0, arr_size)
    ax.set_ylim(-1000000, 1000000)


def update(frame):
    global running
    if not running:
        selectSort(lst4python)
        running = True


ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True)

plt.show()
