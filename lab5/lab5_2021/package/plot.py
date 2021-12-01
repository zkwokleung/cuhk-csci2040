import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random
import myModule


arr_size = 10000  # The size of array and the x limit
low_bound, up_bound = -1000000, 1000000  # The bound of random numbers

# Two excatly same list for 2 sorting method
lst4python = [random.randint(low_bound, up_bound) for _ in range(arr_size)]
lst4C = lst4python.copy()
x = np.arange(0, arr_size)
running = False

# The plot
fig, ax = plt.subplots(nrows=2)

# Python
ax[0].set_title("Sort using Python")
# Hide the X axis since it is overlapping with the graph below
ax[0].get_xaxis().set_visible(False)
ln_python, = ax[0].plot(x, lst4python, "ro")

# C
ax[1].set_title("Sort using C")
ln_C, = ax[1].plot(x, lst4C, "bo")

# Animation function


def init():
    ax.set_xlim(0, arr_size)
    ax.set_ylim(low_bound, up_bound)


def update(frame):
    pass


ani = FuncAnimation(fig, update, frames=np.linspace(0, arr_size, arr_size),
                    init_func=init, blit=True)

plt.show()
