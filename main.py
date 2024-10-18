# task 1
#
# array = [1, 2, 19, 120, -9999, 232, 2]
#
# maxInt = array[0]
# minInt = array[0]
#
# for num in array:
#     if num > maxInt:
#         maxInt = num
#     if num < minInt:
#         minInt = num
#
# print(maxInt - minInt)


# task 2
# import random
#
# arrayLength = 10
# array = []
#
# for _ in range(arrayLength):
#     randomNumber = int((round(random.random(), 2)) * 200) - 100
#     array.append(randomNumber)
# print(array)

# task 3
import random

arrayLength = int(input("Введите размер массива"))
array = []

for _ in range(arrayLength):
    randomNumber = random.randint(-50, 100)
    array.append(randomNumber)

maxInt = array[0]
minInt = array[0]

for num in array:
    if num > maxInt:
        maxInt = num
    if num < minInt:
        minInt = num

print(maxInt, minInt)
# task 4




