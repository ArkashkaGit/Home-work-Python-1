# Задача № 8.
# Напишите программу, 
# которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3


def Number_Quarter():
    while(True):
        x = int(input("Введите координату X : "))
        y = int(input("Введите координату Y : "))

        if(x>0 and y>0):
            print("Коотдинаты точки находится в первой четверти")
            break

        elif(x<0 and y>0):
            print("Координаты точки находятся во второй четверти")
            break

        elif(x<0 and y<0):
            print("Коотдинаты точки находится в третьей четверти")
            break

        elif(x>0 and y<0):
            print("Координаты точки находятся во четвертой четверти")
            break

        else:
            print("координаты точки находятся на оси координат")

Number_Quarter()