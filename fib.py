file_name = "inputFib.txt"
try:
    with open(file_name) as openFile:
        n = int(openFile.read())
except FileNotFoundError:
    print("Incorrect file!")
    exit(-1)
except ValueError:
    print("Incorrect input!")
    exit(-1)
fib1 = fib2 = 1

if n < 2:
    quit()

print(fib1, end=' ')
print(fib2, end=' ')
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
