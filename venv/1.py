
"""3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин."""

import random as rd

def create_graph(nodes):
    graph = {}
    for i in range(nodes):
        graph[i] = {j for j in range(nodes) if i < j}
    return graph


def create_graph_2(nodes):
    graph = {}
    for i in range(nodes):
        graph[i] = set()
        for _ in range(nodes):
            nd = rd.randint(0, nodes-1)
            if nd != i:
                graph[i].add(nd)
    num = rd.randint(0, nodes-1)
    for j in range(num):
        x = graph[rd.randint(0, nodes-1)]
        if len(x) != 0:
            y = list(x)[rd.randint(0, len(x)-1)]
            graph[y].clear()
    return graph


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)  # список посещённых вершин
            stack.extend(graph[node] - visited)  # добавляем к списку вершин новые найденные вершины
    return visited


n = int(input('Введите число вершин: '))
new_graph = create_graph_2(n)
print(f'Граф: {new_graph}')
v = int(input('Введите вершину от которой начать обход: '))
print(dfs(new_graph, v))
# все вершины
all_path = []
for v in range(len(new_graph)):
    all_path.append(dfs(create_graph(n), v))
print('Простой граф', create_graph(n))
print(*all_path, sep='\n')