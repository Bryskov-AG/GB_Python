# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

import random
N = int(input('Введите размер массива N: '))
A_array = []
for i in range(N):
    A_array.append(random.randint(1, N))
print(A_array)

X = int(input('Введите число X: '))

closest = A_array[0]
for i in range(1, N):
    if abs(A_array[i] - X) < abs(closest - X):
        closest = A_array[i]

print(f"Ближайший элемент к числу {X} в массиве A_array: {closest}")

