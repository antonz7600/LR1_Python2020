import itertools
import random


def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def mrg_sort(file_name):
    try:
        # file_name = "input4.txt"
        with open(file_name) as openFile:
            test_arr = [[int(x) for x in line.split()] for line in openFile]
    except FileNotFoundError:
        print("Incorrect file!")
        exit(-1)
    except ValueError:
        print("Incorrect input!")
        exit(-1)
    test_arr = list(itertools.chain(*test_arr))
    print("Unsorted:")
    print(test_arr)
    print("Sorted:")
    mergesort(test_arr)
    print(test_arr)




# test_arr = [random.randint(0, 10000) for num in range(100)]
# print("Unsorted:")
# print(test_arr)
# print("Sorted:")
# mergesort(test_arr)
# print(test_arr)