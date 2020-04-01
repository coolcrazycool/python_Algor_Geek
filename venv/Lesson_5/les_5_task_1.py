from collections import namedtuple


numb = int(input("Введите кол-во предприятий: "))
Enterprise = namedtuple('Enterprise', ['k1', 'k2', 'k3', 'k4'])
enter_tuple = {}

for i in range(numb):
    enterprise_name = input("Введите название предприятия: ")
    enter_tuple[enterprise_name] = Enterprise(int(input("Прибыль 1 квартал: ")), int(input("Прибыль 2 квартал: ")),\
                                   int(input("Прибыль 3 квартал: ")), int(input("Прибыль 4 квартал: ")))

total_profit = {sum(profit) for name, profit in enter_tuple.items()}
average_profit = sum(total_profit) / len(enter_tuple)

print(f"Средняя прибыль для {numb} предприятий: {average_profit}")
print(f"Средняя прибыль больше {average_profit}:")

for name, profit in enter_tuple.items():
    if sum(profit) > average_profit:
        print(f"{name} - {sum(profit)}")

print(f"Средняя прибыль меньше {average_profit}:")

for name, profit in enter_tuple.items():
    if sum(profit) < average_profit:
        print(f"{name} - {sum(profit)}")