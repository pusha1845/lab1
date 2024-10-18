# task 1
#
array = [1, 2, 19, 120, -9999, 232, 2]

maxInt = array[0]
minInt = array[0]

for num in array:
    if num > maxInt:
        maxInt = num
    if num < minInt:
        minInt = num

print(maxInt - minInt)








