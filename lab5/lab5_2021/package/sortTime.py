import myModule
import random
import time

# Define the selection sort in Python


def selectSort(list):
    for i in range(len(list) - 1):
        min_idx = i
        for j in range(i+1, len(list)):
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]

    return list


if __name__ == "__main__":
    # User Input
    flag = True
    while flag:
        arr_size = int(input("Input array size: "))
        if 1 <= arr_size <= 20000:
            flag = False
        else:
            print("Size must be within 1 to 20000.")

    # Generate a random list
    lst = [random.randint(-1000000, 1000000) for _ in range(arr_size)]

    # Test the runtime in C
    start = time.time()
    myModule.selectSort(lst)
    end = time.time()
    print("Time used in C extension selection sort {:.3f}".format(end - start))

    # Test the runtime in python
    start = time.time()
    selectSort(lst)
    end = time.time()
    print("Time used in Python selection sort {:.3f}".format(end - start))
