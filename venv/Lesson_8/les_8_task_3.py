# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

import random


def graph_creator(N):
    gr = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if random.randint(0, 1) == 1 and i != j:
                gr[i].append(j)
    for i in range(N):
        rand_ch = [j for j in range(N) if j != i]
        one_x_gr = sum(gr, [])
        if i not in one_x_gr:
            gr[random.choice(rand_ch)].append(i)
        if len(gr[i]) == 0:
            gr[i].append(random.choice(rand_ch))
    if len(sum(gr, [])) == len(gr) and N > 2:
        i = random.randint(0, N)
        rand_ch = [j for j in range(N) if j != i and j not in gr[i]]
        gr[i].append(random.choice(rand_ch))
    return gr

def dfs(graph, visited, prev, start):
    visited[start] = True
    print(f'Зашли в {start} вершину. Она ведет в вершины: {graph[start]}', end='\n')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, visited, prev, i)


n = int(input("Сколько вершин у графа(больше 1!): "))
my_graph = graph_creator(n)
print(f"Полученный список смежности: {my_graph}")

start = int(input("Введите начальную вершину(с нуля): "))

visited = [False] * len(my_graph)
prev = [None] * len(my_graph)

dfs(my_graph, visited, prev, start)


