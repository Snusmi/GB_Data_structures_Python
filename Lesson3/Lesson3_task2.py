""""
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
(помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.
"""

import random
a = [random.randint(0,100) for _ in range(15)]
indices = []

for i, item in enumerate(a):
    indices.append(i) if item % 2 == 0 else None

print(a)
print(f"Индексы четных элементов\n{indices}")