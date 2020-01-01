""""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
"""
import collections as cs

def sum_and_multiply(a:str, b:str):
    """"
    returns:
        a as list of chars
        b as list of chars
        a + b as list of chars
        a * b as list of chars
    """

    array = "0123456789ABCDEF"
    hex_dict = {a: i for i, a in enumerate(array)}
    hex_dict_reverse = {str(i): a for i, a in enumerate(array)}

    a_dict = cs.OrderedDict()
    for letter in a:
        a_dict[letter] = hex_dict[letter]

    b_dict = cs.OrderedDict()
    for letter in b:
        b_dict[letter] = hex_dict[letter]

    a_dec = 0 # перевод в десятичное
    for i, k in enumerate(a_dict):
        a_dec += a_dict[k] * (16 ** (len(a_dict)-i-1))

    b_dec = 0
    for i, k in enumerate(b_dict):
        b_dec += b_dict[k] * (16 ** (len(b_dict)-i-1))

    sum_dec = a_dec + b_dec # перевод десятичной суммы снова в шестнадцатеричную
    sum_hex = cs.OrderedDict()
    while sum_dec > 0:
        sum_hex[str(sum_dec % 16)] = hex_dict_reverse[str(sum_dec % 16)]
        sum_hex.move_to_end(str(sum_dec % 16), last=False)
        sum_dec = sum_dec // 16

    multiply_dec = a_dec * b_dec
    multiply_hex = cs.OrderedDict()
    while multiply_dec > 0:
        multiply_hex[str(multiply_dec % 16)] = hex_dict_reverse[str(multiply_dec % 16)]
        multiply_hex.move_to_end(str(multiply_dec % 16), last=False)
        multiply_dec = multiply_dec // 16

    return list(a_dict.keys()), list(b_dict.keys()), list(sum_hex.values()), list(multiply_hex.values())

num1 = "A2"
num2 = "C4F"

# Раскомментировать, если нужно попробовать самому
num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")

num1l, num2l, suml, multl = sum_and_multiply(num1, num2)
print(f"Первое число - {num1l}")
print(f"Второе число - {num2l}")
print(f"Их сумма - {suml}")
print(f"Их произведение - {multl}")

