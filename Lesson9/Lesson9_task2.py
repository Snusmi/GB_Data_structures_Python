""""
Закодируйте любую строку по алгоритму Хаффмана.
"""
from collections import Counter, namedtuple
# a = 'beep boop beer!'

def huffman_encode(a:str):

    class Node(namedtuple("Node", ["left", "right"])):
        def walk(self, code, binary):
            self.left.walk(code, binary + "0")
            self.right.walk(code, binary + "1")


    class Leaf(namedtuple("Leaf", ["ch"])):
        def walk(self, code, binary):
            code[self.ch] = binary or "0"

    pre_q = sorted(dict(Counter(a)).items(), key=lambda x: x[1], reverse=True)
    queue = [(Leaf(ch), fr) for ch, fr in pre_q]

    while len(queue) > 1:
        left, fr1 = queue.pop()
        right, fr2 = queue.pop()
        queue.append((Node(left, right), fr1+fr2))
        queue = sorted(dict(queue).items(), key=lambda x: x[1], reverse=True)

    [(root, fr)] = queue
    code = {}
    root.walk(code, "")

    encoded = "".join(code[ch] for ch in a)
    return code, encoded

my_string = input('Что кодируем? ')
codes, encoded_string = huffman_encode(my_string)
print(f"Кодировка отдельных символов: {codes}")
print(f"Закодированная строка: {encoded_string}")
