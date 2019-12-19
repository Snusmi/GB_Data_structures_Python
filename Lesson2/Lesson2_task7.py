""""
Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""

def my_sum(n):
    return n + my_sum(n - 1) if n > 0 else 0

def formula(n):
    return n * (n + 1) / 2


def is_equal(n):
    """"
    возвращает True, если выполняется равенство для конкретного n, иначе False
    """
    return my_sum(n) == formula(n)


def is_equal_range(n):
    """"
    возвращает True, если выполняется равеноство для натуральных чисел от 1 до n
    выводит на экран проверку равенства для каждого n
    """
    eval = True
    for i in range(1, n+1):
        eval = eval and is_equal(n)
        print(f"n={i} - {eval}")
    return eval

print(is_equal_range(int(input("Введите, до какого n проверить выполнимость равенства: "))))