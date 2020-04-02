# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

N = int(input("Кол-во друзей: "))
hand_shakes = 0
hand_graph = [[1 for _ in range(N)] for _ in range(N)]

for id, value in enumerate(hand_graph):
    for id_d, v in enumerate(value):
        if id == id_d:
            hand_graph[id][id_d] = 0
        if hand_graph[id][id_d] == 1:
            hand_shakes += 1

print(f'Кол-во рукопожатий: {int(hand_shakes/2)}')