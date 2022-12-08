# Sem5

import random

matrix = 5
mapLength = range(matrix)
mapComputer = [[' ' for i in mapLength] for y in mapLength]
mapPlayer = [[' ' for i in mapLength] for y in mapLength]

# Показать разделитель
def printLiner():
    print("_ " * len(mapLength))
# Показать карту
def showMap(mapItem):
    printLiner()
    # показать колонки
    for row in mapLength:
        print(row, end=" ")
    print()
    print("_ " * len(mapLength))

    for column in range(len(mapItem)):
        for row in range(len(mapItem[column])):
            print(mapItem[column][row], end=" ")
        # показать строки
        print(" | ", column)
    printLiner()

# Создаем корабли
def generateComputerMap(mapItem, count = 1):
    global matrix
    comp_ship_points = count
    comp_filled_points = []

    while len(comp_filled_points) < comp_ship_points:
        column = random.randint(0, matrix - 1)
        row = random.randint(0, matrix - 1)

        isExist = False
        for v in comp_filled_points:
            if str(v) == str((column, row)):
                isExist = True
                break
                
        if isExist:
            continue
        else:
            comp_filled_points.append((column, row))

    print(comp_filled_points)
    for i in range(len(comp_filled_points)):
        mapItem[comp_filled_points[i][1]][comp_filled_points[i][0]] = "*"
                        
    return mapItem


# начало игры
points = 4
pointsFinded = []
mapComputer = generateComputerMap(mapComputer, points)
isGame = True

# что бы вывести карту противника
showMap(mapComputer)

while isGame:
    x = int(input("Кордината X: ") or 0)
    y = int(input("Кордината Y: ") or 0)

    if (x >= 0 and x <= matrix and y >= 0 and y <= matrix):
        if mapComputer[y][x] == "*":
            mapPlayer[y][x] = "*"
            if [y, x] not in pointsFinded:
                pointsFinded.append([y, x])
            showMap(mapPlayer)
            print("Попадание!")
        else:
            mapPlayer[y][x] = "-"
            showMap(mapPlayer)
            print("Мимо (((")

        if (len(pointsFinded) == points):
            showMap(mapPlayer)
            print("Победа!")
            isGame = False
