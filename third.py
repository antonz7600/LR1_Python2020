import itertools
import random


def qsort(arr, first, last):
    if first >= last:
        return
    mid_index = (first + last) // 2
    if arr[mid_index] < arr[first]:
        arr[mid_index], arr[first] = arr[first], arr[mid_index]
    if arr[last] < arr[first]:
        arr[last], arr[first] = arr[first], arr[last]
    if arr[mid_index] < arr[last]:
        arr[mid_index], arr[last] = arr[last], arr[mid_index]
    mid = arr[last]
    i = first
    j = last
    while i <= j:
        while arr[i] < mid:
            i += 1
        while arr[j] > mid:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i, j = i + 1, j - 1
    qsort(arr, first, j)
    qsort(arr, i, last)


test_arr = [random.randint(0, 10000) for num in range(100000)]
print("Unsorted:")
print(test_arr)
qsort(test_arr, 0, len(test_arr) - 1)
print("Sorted:")
print(test_arr)
file_name = "input4.txt"
print("Unsorted:")
try:
    with open(file_name) as openFile:
        test_arr = [[int(x) for x in line.split()] for line in openFile]
except FileNotFoundError:
    print("Incorrect file!")
    exit(-1)
except ValueError:
    print("Incorrect input!")
    exit(-1)
test_arr = list(itertools.chain(*test_arr))
print(test_arr)
qsort(test_arr, 0, len(test_arr) - 1)
print("Sorted:")
print(test_arr)
