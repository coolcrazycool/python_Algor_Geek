# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.

gr = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]

def way_mapping(id, parent, way, i, spam_start):
    if parent[id] == spam_start:
        return spam_start
    else:
        way[i].append(parent[id])
        return way_mapping(parent[id], parent, way, i, spam_start)



def deikstra(graph, start):
    spam_start = start
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    way = [[] for _ in range(length)]
    if spam_start not in parent:
        way = [["Нет пути!!!"] for _ in range(length)]
    else:
        for id, vertex in enumerate(parent):
            if vertex == -1:
                if spam_start == id:
                    way[id].append("Корень")
                else:
                    way[id].append("Недостижима")
            else:
                way[id].append(id)
                way[id].append(way_mapping(id, parent, way, id, spam_start))
            way[id].reverse()

    return cost, way


s = int(input("От какой точки идти: "))
my_cost, my_way = deikstra(gr, s)

for i in range(len(gr)):
    print(f"Стоимость пути до вершины {i} = {my_cost[i]}, кратчаший маршут до нее(включая саму вершину) - {my_way[i]}")
