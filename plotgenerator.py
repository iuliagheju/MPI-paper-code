import numpy as np
import time
import matplotlib.pyplot as plt

# Define the sorting algorithms

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    # Shell Sort
    def shellSort(arr):
        n = len(arr)
        gap = n//2

    while gap > 0:

        for i in range(gap,n):
            temp = arr[i]
            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2


# Generate a random array
np.random.seed(0)
arr = np.random.randint(0, 100, size=100).tolist()

# Measure the sorting times
algorithms = {'Bubble Sort': bubble_sort, 'Insertion Sort': insertion_sort,
              'Selection Sort': selection_sort, 'Merge Sort': merge_sort,
              'Quick Sort': quick_sort}

times = {}
for name, func in algorithms.items():
    copy_arr = arr.copy()
    start_time = time.time()
    func(copy_arr)
    end_time = time.time()
    times[name] = end_time - start_time

# Plot the comparison
plt.bar(times.keys(), times.values(), color='skyblue')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Performance')
plt.xticks(rotation=45)
plt.show()