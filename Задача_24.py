# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.




import random
shrub = int(input("Введите количество кустов: "))
berries = list(random.randint(1, 10) for i in range(shrub))
result = []
i = 0
sum = 0

print(berries)

while (i < shrub):
    if (i == shrub - 1):
        sum = berries[i] + berries[i - 1] + berries[0]
    else:
        sum = berries[i] + berries[i - 1] + berries[i + 1]
        result.append(sum)
        result.sort()
    i += 1

print(f"Максимальное число собранных ягод за один заход {result[-1]}")