# lab1_task2.py
# Задание 2: квадраты чисел от a до b

a, b = map(int, input("Введите два числа a и b (a ≤ b): ").split())

for i in range(a, b + 1):
    print(f"{i}^2 = {i ** 2}")
