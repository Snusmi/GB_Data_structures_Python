""""
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
"""
try:
    x1 = float(input("Введите координату x первой точки: "))
    y1 = float(input("Введите координату y первой точки: "))
    x2 = float(input("Введите координату x второй точки: "))
    y2 = float(input("Введите координату y второй точки: "))

    if x1 == x2:
        if y1 == y2:
            print("Точки совпадают, введите координаты разных точек")
        else:
            print("x = {} - уравнение прямой, проходящей через точки ({}, {}) и ({}, {})".format(x1, x1, y1, x2, y2))
    else:
        if y1 == y2:
            print("y = {} - уравнение прямой, проходящей через точки ({}, {}) и ({}, {})".format(y1, x1, y1, x2, y2))
        else:
            k = (y2 - y1) / (x2 - x1)
            b = y2 - k * x2
            print("y = {}x + {} - уравнение прямой, проходящей через точки ({}, {}) и ({}, {})".format(k, b, x1, y1, x2, y2))
except ValueError:
    print("Нужно вводить число")

