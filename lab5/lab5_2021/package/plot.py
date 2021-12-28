import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random
import myModule


# Controlable variables
# User Input
flag = True
while flag:
    arr_size = int(input("Input array size: "))
    if 1 <= arr_size <= 20000:
        flag = False
    else:
        print("Size must be within 1 to 20000.")
low_bound, up_bound = -1000000, 1000000  # The bound of random numbers


# Define the selection sort in Python
def selectSort(list):
    for i in range(len(list) - 1):
        min_idx = i
        for j in range(i+1, len(list)):
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]

    return list


# Modified selectSort to store every intermediate step to a list
def selectSortMod(list):
    for i in range(len(list)):
        min_idx = i
        for j in range(i+1, len(list)):
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
        steps.append(list[::])


# Generate a random list
lst = [random.randint(low_bound, up_bound)
       for _ in range(arr_size)]

# Test the runtime in C
start = time.time()
myModule.selectSort(lst)
end = time.time()
time_C = end - start  # Time taken to perform the sort in C

# Test the runtime in python
start = time.time()
selectSort(lst)
end = time.time()
time_python = end - start  # Time taken to perform the sort in python

# Runtime variables
steps = []  # An array to store the intermediate steps
ratio = time_python / time_C  # the ratio
origin_lst = [random.randint(low_bound, up_bound)
              for _ in range(arr_size)]  # list for sorting
x = np.arange(0, arr_size)  # The x value for the plot


# get the intermediate steps
selectSortMod(origin_lst)
# steps = steps[::100]  # Skipping some steps to speed up the animation
# The y value for the Python plot. Skipped some of the steps to increase the speed
lst4python = steps[::10]
lst4python.append(steps[-1])  # Append the last step in case it dosent include
# The y value for the C plot. Skipping some steps to visualize the speed differences
lst4C = steps[::int(ratio)]
lst4C.append(steps[-1])  # Append the last step in case it dosent include


# The plot
fig, ax = plt.subplots(nrows=2)

# Python
ax[0].set_title("Sort using Python")
# Hide the X axis since it is overlapping with the graph below
ax[0].get_xaxis().set_visible(False)
ax[0].ticklabel_format(useOffset=False, style='plain')
ln_python, = ax[0].plot(x, lst4python[0], "ro", markersize=2)

# C
ax[1].set_title("Sort using C")
ax[1].ticklabel_format(useOffset=False, style='plain')
ln_C, = ax[1].plot(x, lst4C[0], "bo", markersize=2)


# Animation function
def init():
    ax[0].set_xlim(0, arr_size)
    ax[0].set_ylim(low_bound, up_bound)

    ax[1].set_xlim(0, arr_size)
    ax[1].set_ylim(low_bound, up_bound)
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
