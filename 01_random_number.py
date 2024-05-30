

import random

# Функция для проверки является ли число простым
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Генератор случайных чисел в заданном диапазоне
def random_generator(start, end):
    while True:
        yield random.randint(start, end)

# Отфильтровываем числа с числом делителей больше n
def filter_numbers(numbers, n):
    return filter(lambda x: len([i for i in range(1, x+1) if x % i == 0]) <= n, numbers)

# Создаем генератор случайных чисел
numbers = random_generator(1, 100)

# Отфильтровываем числа с числом делителей больше 5
filtered_numbers = filter_numbers(numbers, 2)

# Выводим первые 10 отфильтрованных чисел
for _ in range(1):
    print(next(filtered_numbers))
