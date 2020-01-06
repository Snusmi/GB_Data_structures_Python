""""
тсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""

""""
1. Разбитие массива на мелкие части одинакового размера. Рекурсивно массив разбивается пока у нас не будет отдельных элементов
2. Сливаем части “соседних массивов” в один с сортировкой. 
Опять же, сортировка проходит достачтоно интересно: так как мы сливаем уже сортированные массивы — в результате хотелось бы получить сортированный массив. 

Итак, допустим у нас есть два массива:
2.1 Указатели указывают на первый элемент обоих массивов. Выбирается наименьший из них
2.2 В массиве в котором было наименьшее число — указатель переноситься на следующий элемент. Повторяем пункт 2.1
2.3 Если в одном из массивов закончились элементы — переносим элементы другого массива в наш отсортированный массив (слив остатков)
3. Повторяем пока подмасивы не закончатся (c)

Худшее время	O(n log2 n)
Лучшее время	O(n log2 n)
Среднее время	O(n log2 n)
Затраты памяти	O(n) вспомогательных
"""
import random

array = [random.uniform(0,50) for i in range(10)]
print(array)

def merge_sort(array):

    def _sort(left, right):
        _result = []
        ileft = 0
        iright = 0

        while ileft < len(left) and iright < len(right):
            if left[ileft] < right[iright]:
                _result.append(left[ileft])
                ileft += 1
            else:
                _result.append(right[iright])
                iright += 1

        while ileft < len(left):
            _result.append(left[ileft])
            ileft += 1

        while iright < len(right):
            _result.append(right[iright])
            iright += 1

        return _result

    if len(array) <= 1:
        return array
    else:
        left = array[:len(array)//2]
        right = array[len(array)//2:]
        result = _sort(merge_sort(left), merge_sort(right))
    return result

new_array = merge_sort(array)
print(new_array)