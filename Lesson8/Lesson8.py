from collections import deque

g = [
    [0,1,1,0,1,0,0,0],
    [1,0,0,0,0,0,0,0],
    [1,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0],
    [1,0,1,0,0,0,1,0],
    [0,0,0,1,0,0,1,1],
    [0,0,0,0,1,1,0,1],
    [0,0,0,0,0,1,1,0]
]

def bfs(graph, start, finish):
    parent = [None for i in range(len(graph))]
    is_visited = [False for i in range(len(graph))]
    is_visited[start] = True

    deq = deque([start])

    while len(deq) > 0:
        current = deq.pop()

        if current == finish:
            break
        else:
            for i, vertex in enumerate(graph[current]):
                if vertex == 1 and not is_visited[i]:
                    is_visited[i] = True
                    parent[i] = current
                    deq.appendleft(i)
    else:
        return f"Из вершины {start} в вершину {finish} попасть нельзя"

    cost = 0
    way = deque([finish])
    i = finish
    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.appendleft(start)

    return f"Кратчайший путь {list(way)} стоимостью {cost} условных единиц"

print(bfs(g,2,5))