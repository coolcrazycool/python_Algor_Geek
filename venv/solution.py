while True:
    # input
    try:
        n = int(input('Введите количество друзей: '))
    except ValueError:
        print('Ошибка ввода!')
        continue
    graph = []
    handshakes = 0
    # graph initialize and count
    for i in range(n):
        friend = [i + 1 for i in range(n)]
        friend[i] = 0
        graph.append(friend)
    print('Граф: ', sep="/n")
    print(graph, sep="/n")
    for i, friend in enumerate(graph):
        for handshake in friend:
            if handshake != 0:
                handshakes += 1
                graph[handshake - 1][i] = 0
    print(f'Количество рукопожатий: {handshakes}')
    break