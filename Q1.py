import timeit
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

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
    return arr

# List of input sizes to test
input_sizes = list(range(1, 200, 5))
print(input_sizes)

# Template for setup code used by timeit
setup_template = '''
from __main__ import insertion_sort, merge_sort
import random
random.seed(0)
data = [random.randint(0, 99999) for _ in range({size})]
'''

insertion_sort_times = []
merge_sort_times = []
for size in input_sizes:
    setup_code = setup_template.format(size=size)

    insertion_sort_time = timeit.timeit('insertion_sort(data[:])', setup=setup_code, number=1000)

    merge_sort_time = timeit.timeit('merge_sort(data[:])', setup=setup_code, number=1000)

    print(f"Size {size}: Insertion Sort time = {insertion_sort_time}, Merge Sort time = {merge_sort_time}")

    insertion_sort_times.append(insertion_sort_time)
    merge_sort_times.append(merge_sort_time)



plt.figure(figsize=(12, 8))
plt.plot(input_sizes, insertion_sort_times, label='Insertion Sort', marker='o')
plt.plot(input_sizes, merge_sort_times, label='Merge Sort', marker='x')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time Comparison: Insertion Sort vs. Merge Sort')
plt.legend()
plt.grid(True)


plt.legend()
plt.savefig('Q1.png', dpi=300)

