# Задача №33. 
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

list = [1, 3, 3, 3, 4]
mi = min(list)
ma = max(list)
for i in range(5):
   if list[i] == ma:
      list[i] = mi
print(list)