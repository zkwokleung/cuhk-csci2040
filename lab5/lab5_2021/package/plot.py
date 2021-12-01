import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random


# Controlable variables
time_python = 8.206  # Time taken to perform the sort in python
time_C = 0.037  # Time taken to perform the sort in C
arr_size = 10000  # The size of array and the x limit
low_bound, up_bound = -1000000, 1000000  # The bound of random numbers

# Runtime variables
steps = []  # An array to store the intermediate steps
ratio = time_python / time_C  # the ratio
origin_lst = [random.randint(low_bound, up_bound)
              for _ in range(arr_size)]  # list for sorting
x = np.arange(0, arr_size)  # The x value for the plot


# Modified selectSort to store every intermediate step to a list
def selectSort(list):
    for i in range(len(list)):
        min_idx = i
        for j in range(i+1, len(list)):
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
        steps.append(list[::])


# get the intermediate steps
selectSort(origin_lst)
# steps = steps[::100]  # Skipping some steps to speed up the animation
lst4python = steps[::]  # The y value for the Python plot
# The y value for the C plot. Skipping some steps to visualize the speed differences
lst4C = steps[::int(ratio)]
lst4C.append(steps[-1])  # Append the last step in case it dosent include


# The plot
fig, ax = plt.subplots(nrows=2)

# Python
ax[0].set_title("Sort using Python")
# Hide the X axis since it is overlapping with the graph below
ax[0].get_xaxis().set_visible(False)
ln_python, = ax[0].plot(x, lst4python[0], "ro")

# C
ax[1].set_title("Sort using C")
ln_C, = ax[1].plot(x, lst4C[0], "bo")


# Animation function
def init():
    ax[0].set_xlim(0, arr_size)
    ax[0].set_ylim(low_bound, up_bound)
    ax[0].ticklabel_format(useOffset=False)

    ax[1].set_xlim(0, arr_size)
    ax[1].set_ylim(low_bound, up_bound)
    ax[1].ticklabel_format(useOffset=False)
    return [ln_python, ln_C]


def update(frame):
    ln_python.set_data(x, lst4python[frame])
    if frame >= len(lst4C):
        # Display the last frame for the c plot
        ln_C.set_data(x, lst4C[-1])
    else:
        ln_C.set_data(x, lst4C[frame])
    return [ln_python, ln_C]


ani = FuncAnimation(fig, update, frames=range(len(steps)),
                    init_func=init, blit=True, repeat=False, interval=1)

plt.show()
