# Задача 9.
# По данному целому неотрицательному n вычислите значение n!. N! = 1*2*3...*N(произведение всех чисел от 1 до N) 0! = 1.
# решить через While      
# input  5           
# Output  120

# N = int(input('Введите число : '))
# print(N)

# i = int(1)
# while N > 1:
#     i *=N
#     N -=1
# print(i)

    
# Задача 11.
# Дано натуральное число А>1.Определите,каким по счёту числом Фибоначчи оно является,
# то есть выведите такое число n ,что ф(n)= А.Если А не является числом Фибоначчи,выведите число -1. 
# input-5   output-6


# A = int(input('Введите число : '))
# fib1 = 1
# fib2 = 1
# i = 3
# if A == fib1: print("№1")
# while A >= i:
#     fibsum = fib1 + fib2
#     fib1=fib2
#     fib2=fibsum
#     if fibsum == A:
#         print(f"№{i+1}")
#         break

#     elif A < fibsum:
#         print("-1")
#         break
#     else: i += 1


# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
#  Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. 
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50

# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2


# import random
# n = int(input('Введите количество дней : '))
# i = 0
# x = 0
# list = []
# listCount = []
# while n > i:
#     list.append(random.randint(-50,51))
#     i+=1
# print(list)

# for j in range (0,n):
#     if list[j] > 0:
#         x+=1
#     else:
#         listCount.append(x)
#         x = 0
# listCount.append(x)

# print(max(listCount))
# print(listCount)



# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
# Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# import random
# n = int(input("Введите кол-во арбузов на рынке: "))
# list = []
# i = 0
# for _ in range (n):
#     list.append(random.randint(5, 20))
# max = list[i]
# min = list[i]
# while n > i:
#     if list[i] < min:
#         min = list[i]
#     if list[i] > max:
#         max = list[i]
#     i = i + 1
# print(list)
# print(f"Минимальный {min}, Максимальный {max}")



#Напечатать двухзначные числа кратные 4, но не кратные 6

# i = 10
# while 100 > i:
#     if i%4 == 0 and i%6 != 0:
#         print(i,end=" ")
#     i+=1