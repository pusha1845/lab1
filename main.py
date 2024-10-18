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
# array = [
#     [],
#     [],
#     []
# ]
#
# # rows
# rowSums = []
# lenItemArray = 5
#
# for i in range(len(array)):
#     for _ in range(lenItemArray):
#         randomNumber = random.randint(-100, 100)
#         array[i].append(randomNumber)
#     print(array[i])
#
#
# for row in array:
#     rowSum = 0
#     for element in row:
#         rowSum += element
#     rowSums.append(rowSum)
# print(rowSums)
#
# #cols
# lenCols = len(array[0])
# lenRows = len(array)
#
# colsSums = []
# for col in range(lenCols):
#     colsSum = 0
#     for row in range(lenRows):
#         colsSum += array[row][col]
#     colsSums.append(colsSum)
# print(colsSums)


# task 5

class Student:
    def __init__(self, famil, name, facult, nomZach):
        self.famil = famil
        self.name = name
        self.facult = facult
        self.nomZach = nomZach

def inputStudents():
    students = []
    for _ in range(1):
        famil = input("Введите фамилию студента: ")
        name = input("Введите имя студента: ")
        facult = input("Введите факультет студента: ")
        nomZach = int(input("Введите номер зачётной книжки студента: "))
        students.append(Student(famil, name, facult, nomZach))
    return students

def printStudents(students):
    for student in students:
        print(f"Студент {student.famil} {student.name} обучается на факультете {student.facult}, номер зачётной книжки {student.nomZach}")

def searchStudent(students, famil=None, name=None, facult=None, nomzach=None):
    for student in students:
        if ((famil is None or student.famil == famil) and
            (name is None or student.name == name) and
            (facult is None or student.facult == facult) and
            (nomzach is None or student.nomZach == nomzach)):
            return student
    return None

def main():
    students = inputStudents()
    printStudents(students)

    # Поиск студента
    searchFamil = input("Введите фамилию для поиска (или оставьте пустым - поиск по этому полю осуществляться не будет): ")
    searchName = input("Введите имя для поиска (или оставьте пустым - поиск по этому полю осуществляться не будет): ")
    searchFacult = input("Введите факультет для поиска (или оставьте пустым - поиск по этому полю осуществляться не будет): ")
    searchNomzach = input("Введите номер зачётной книжки для поиска (или оставьте пустым - поиск по этому полю осуществляться не будет): ")
    searchNomzach = int(searchNomzach) if searchNomzach.isdigit() else searchNomzach


    foundStudent = searchStudent(students, searchFamil or None, searchName or None, searchFacult or None, searchNomzach or None)

    if foundStudent:
        print(f"Найден студент: {foundStudent.famil} {foundStudent.name}, факультет {foundStudent.facult}, номер зачётной книжки {foundStudent.nomZach}")
    else:
        print("Студент не найден.")

if __name__ == "__main__":
    main()





