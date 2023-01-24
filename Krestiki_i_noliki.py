import random

print("        КРЕСТИКИ И НОЛИКИ\n")

#Создание игрового поля
matrix = [[" "," "," "],
          [" "," "," "],
          [" "," "," "]]



def print_table():
    _00 = matrix[0][0]
    _01 = matrix[0][1]
    _02 = matrix[0][2]
    _10 = matrix[1][0]
    _11 = matrix[1][1]
    _12 = matrix[1][2]
    _20 = matrix[2][0]
    _21 = matrix[2][1]
    _22 = matrix[2][2]
    Print_table = (f'''           1   2   3

      1    {_00}   {_01}   {_02}

      2    {_10}   {_11}   {_12}

      3    {_20}   {_21}   {_22}    ''')


    return print(Print_table)



#Присваивание имен и фигур игрокам
Pl_1 = input("\nВведите имя первого игрока")
rlist = ["X","O"]
Pl_1_1 = random.choice(rlist)
if Pl_1_1 == "X":
    print("Вы играете крестиками")
else:
    print("Вы играете ноликами")

Pl_2 = input("Введите имя второго игрока")
if Pl_2 == Pl_1:
    Pl_2 += "_2"
if Pl_1_1 == "X":
    Pl_2_2 = "0"
else:
    Pl_2_2 = "X"
if Pl_2_2 == "X":
    print("Вы играете крестиками")
else:
    print("Вы играете ноликами")

print_table()

#Функция победы
def win_(a):
    if matrix[0][0] == matrix[0][1] == matrix[0][2] == a or matrix[1][0] == matrix[1][1] == matrix[1][2] == a or matrix[2][0] == matrix[2][1] == matrix[2][2] == a or matrix[0][0] == matrix[1][0] == matrix[2][0] == a or matrix[0][1] == matrix[1][1] == matrix[2][1] == a or matrix[0][2] == matrix[1][2] == matrix[2][2] == a or matrix[0][0] == matrix[1][1] == matrix[2][2] == a or matrix[2][0] == matrix[1][1] == matrix[0][2] == a:
       return True

#Функция ничьи
def pat_():
    if " " in matrix[0] or " " in matrix[1] or " " in matrix[2]:
        return True

#Начало игры

#Функция выбора строки
def stro():
    strok = input("введите строку")
    if strok != "1" and strok != "2" and strok !="3":
        print("такой строки не существует")
        return stro()
    return int(strok)

#Функция выбора столбца
def stol():
    stolb = input("введите столбeц")
    if stolb != "1" and stolb != "2" and stolb != "3":
        print("такого столбца не существует")
        return stol()
    return int(stolb)

def loc_X(a,b):  # Функция внесения Х в клетку
    global matrix
    if matrix[a - 1][b - 1] == "X" or matrix[a - 1][b - 1] == "0":
        print("Ячейка уже занята")
        return False
    else:
        matrix[a - 1][b - 1] = "X"
        return True

def loc_0(a,b):  # Функция внесения 0 в клетку
    global matrix
    if matrix[a - 1][b - 1] == "X" or matrix[a - 1][b - 1] == "0":
        print("Ячейка уже занята")
        return False
    else:
        matrix[a - 1][b - 1] = "0"
        return True

while True:
    if Pl_1_1 == "X":#Если первый игрок играет крестиком
        while True:
            print("Ходит " + Pl_1)
            while True:
                y = loc_X(a=stro(), b=stol())
                if y == True:
                    print_table()
                    break
            if win_(Pl_1_1) == True:
                print("Победил игрок " + Pl_1)
                break
            if pat_() != True:
                print("Ничья")
                break
            print("Ходит " + Pl_2)
            while True:
                y = loc_0(a=stro(), b=stol())
                if y == True:
                    print_table()
                    break
            if win_(Pl_2_2) == True:
                print("Победил игрок " + Pl_2)
                break
            if pat_() != True:
                print("Ничья")
                break
    else:#Если второй игрок играет крестиком
        while True:
            print("Ходит " + Pl_2)
            while True:
                y = loc_X(a=stro(), b=stol())
                if y == True:
                    print_table()
                    break
            if win_(Pl_2_2) == True:
                print("Победил игрок " + Pl_2)
                break
            if pat_() != True:
                print("Ничья")
                break
            print("Ходит " + Pl_1)
            while True:
                y = loc_0(a=stro(), b=stol())
                if y == True:
                    print_table()
                    break
            if win_(Pl_1_1) == True:
                print("Победил игрок " + Pl_1)
                break
            if pat_() != True:
                print("Ничья")
                break
    if input("Чтобы начать сначала введите 1\nЧтобы закончить игру введите любое значение") != "1":
        break
    else:
        matrix = [[" ", " ", " "],
                  [" ", " ", " "],
                  [" ", " ", " "]]
        print_table()
