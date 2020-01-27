""""
На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""

n = int(input("Сколько друзей было? "))

def make_g(n):
    """"
    Полный граф c n вершинами
    """
    g = [[1] * n for i in range(n)]
    for i in range(n):
        g[i][i] = 0

    return g

def handshakes(graph):
    len_g = len(graph)
    is_visited = [False] * len_g
    all_shakes = 0

    for current in range(len_g):
        for i, vertex in enumerate(graph[current]):
            if vertex != 0 and not is_visited[i]:
                all_shakes += vertex
                is_visited[current] = True

    return all_shakes

for i in range(n):
    print(make_g(n)[i])
print(f"Число уникальных рукопожатий для {n} друзей равно {handshakes(make_g(n))}")