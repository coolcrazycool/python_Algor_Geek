# 6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

a = float(input("Введите длину 1 стороны: "))
b = float(input("Введите длину 2 стороны: "))
c = float(input("Введите длину 3 стороны: "))

if a+b>c and b+c>a and a+c>b:
    print("Треугольник существует")
else:
    print("Треугольник не существует")