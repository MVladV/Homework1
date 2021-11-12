import os
import random
import timeit


# class Test:

    # str1 = [x ** 2 for x in range(10)]  # заповнення масиву через генератор(швидше)
    # print(str1)
    # list = []

    # for i in range(10):  # заповнення масиву через цикл
    #    list.append(i * i)
    #    print(list)

    # x = open("test.txt", "w+") # заповнення масиву числами до певного розміру
    # x.truncate()
    # while os.path.getsize("test.txt") < 52428800:  # 50 MB
    # x.write(str(random.randrange(1000)) + "\n")

test = """
sum = 0
x = open("test.txt", "r")
for line in x:
    if line.strip().isdigit():
        sum += int(line)
x.close()
"""

print(timeit.timeit(test, number=1)) # час роботи

test = """ # найшкидший варіант
sum = 0
x = open("test.txt", "r")
lines = x.readlines()
for line in lines:
    if line.strip().isdigit():
        sum += int(line)
x.close()
"""

print(timeit.timeit(test, number=1))

test = """
file = open("test.txt", "r")
nums = (int(line.strip()) for line in file if line.strip().isdigit())
sum1 = sum(nums)
file.close()
"""

print(timeit.timeit(test, number=1))
