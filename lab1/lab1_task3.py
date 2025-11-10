# lab1_task3.py
# Задание 3: сумма квадратов чисел от a до b

a, b = map(int, input("Введите два числа a и b (a ≤ b): ").split())

total = sum(i ** 2 for i in range(a, b + 1))
print(f"Сумма квадратов от {a} до {b} = {total}")
