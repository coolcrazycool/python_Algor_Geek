# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

N = int(input("Кол-во друзей: "))
hand_shakes = 0
hand_graph = [[i for i in range(1, N+1)] for _ in range(N)]

for id, value in enumerate(hand_graph):
    for id_d, value_d in enumerate(value):
        if id == id_d:
            hand_graph[id][id_d] = 0
            print(value)

for id, value in enumerate(hand_graph):
    for id_d, value_d in enumerate(value):
        if value[id_d] != 0:
            hand_shakes += 1
            hand_graph[value_d-1][id] = 0

print(f'Кол-во рукопожатий: {hand_shakes}')