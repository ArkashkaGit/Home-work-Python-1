# Задача № 9.
# Напишите программу, 
# которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

while(True):
    Quarter = int(input("Введите номер четверти: "))

    if (Quarter == 1):
        print("Возможный диапазон координат точки (X, Y)")
        break
    elif (Quarter == 2):
        print("Возможный диапазон координат точки (-X, Y)")
        break
    elif (Quarter == 3):
        print("Возможный диапазон координат точки (-X, -Y)")
        break
    elif (Quarter == 4):
        print("Возможный диапазон координат точки (X, -Y)")
        break
    else:
        print("Такой четверти не существует, попробуйте ввести ещё раз")