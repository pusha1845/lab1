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
# import random
#
# arrayLength = int(input("Введите размер массива"))
# array = []
#
# for _ in range(arrayLength):
#     randomNumber = random.randint(-50, 100)
#     array.append(randomNumber)
#
# maxInt = array[0]
# minInt = array[0]
#
# for num in array:
#     if num > maxInt:
#         maxInt = num
#     if num < minInt:
#         minInt = num

# print(maxInt, minInt)
# task 4
array = [
    [],
    [],
    []
]

# rows
rowSums = []
lenItemArray = 5

for i in range(len(array)):
    for _ in range(lenItemArray):
        randomNumber = random.randint(-100, 100)
        array[i].append(randomNumber)
    print(array[i])


for row in array:
    rowSum = 0
    for element in row:
        rowSum += element
    rowSums.append(rowSum)
print(rowSums)

#cols
lenCols = len(array[0])
lenRows = len(array)

colsSums = []
for col in range(lenCols):
    colsSum = 0
    for row in range(lenRows):
        colsSum += array[row][col]
    colsSums.append(colsSum)
print(colsSums)







