from __future__ import division
import math


def fib_gen(file_name):
    try:
        with open(file_name) as openFile:
            n = int(openFile.read())
    except FileNotFoundError:
        print("Incorrect file!")
        exit(-1)
    except ValueError:
        print("Incorrect input!")
        exit(-1)
    for i in range(2, n + 1):
        print(int(((math.sqrt(5) + 1) / 2) ** i / (math.sqrt(5) + 0.5)), end=" ")
