# a = 5
# b = 2.5
# c = 'hello'
# print(a,b,c)  => (5 2.5 hello)
# print(a,'-',b,'-',c)  => (5 - 2.5 - hello)
# print(f"{a}-{b}-{c}")   => (5 - 2.5 - hello)
# print("{}-{}-{}".format(a,b,c))  => (5 - 2.5 - hello)

##############################################################
# Приглашение к вводу:
# print('Введите первое число:' )
# a = input()  => (4)
# b = input('Введите второе число: ')  => (5)

# print(a, '+' , b, '=' , a + b)   => (4 + 5 = 45)


# print('Введите первое число:' )
# a = int(input())                           => (4)
# b = int(input('Введите второе число: '))   => (5)

# print(a, '+' , b, '=' , a + b)             => (4+5=9)

################################################################

# Приводим к целому значению-- Округляем(в меньшую сторону)

# c = 5.89
# print(c)  => (5.89)
# n = int(c)
# print(n)  => (5)

##################################################################

# Посмотреть тип данных

# c = 5.89
# print(c)        =>  (5.89)
# print(type(c))  => (<class 'float'>)

####################################################################

# Арифметические операции:
# +   Сложение
# -   Вычитание
# *   Умножение
# /   Деление(по умолчанию в вещественных числах)
# %   Остаток от деления
# //  Целочисленное деление
# **  Возведение в степень

##################################################################

# Логические операции:
# >   Больше
# >=  Больше или равно
# <   Меньше
# <=  Меньше или равно
# ==  Равно(проверяет равны ли числа)
# !=  Не равно(проверяет,не равны ли значения)
# not Не(отрицание)
# and И(коньюнкция)
# or  Или(дизьюнкция)

################################################################


# Округление

# a=5.67664
# b=7.884756
# print(round(a*b, 3))   => (44.759)  ---сокращает количество знаков после запятой до 3

####################################################################

# Используем flag как условие для завершения работы цикла

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0:  # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делитель числа не может превышать введённое число,делённое на 2
#         print(n)
#         flag = False
#     i += 1

#####################################################################

# Цикл for используем для перебора значений

# for i in 1,-2,3,14,5:
#     print(i)  =>  (1,-2,3,14,5) выводит в столбик

##############################################################

# Цикл for,функция range()

# range выдаёт значения  из диапазона с шагом 1
# если указано только одно число-от 0 до заданного числа(не включая)
# если нужен другой шаг,третьим аргументом можно задать приращение

# r = range(5)  => 0 1 2 3 4   от 0 до 4(5 не включаем)
# r = range(2,5)  => 2 3 4     начиная с 2 до 4(5 не включаем)
# r = range(0,-5)  => -----     от 0 до 5 с конца(от 0 до 0)
# r = range(1,10,2)  => 1 3 5 7 9  от 1 до 9(10 не включаем) с шагом 2
# r = range(100,0,-20)  => 100 80 60 40 20  от 100 до 0(не включая) с шагом -20(с конца)

# for i in r:
#     print(i)

#################################################################

# a = 'qwerty'
# for i in a:
#     print(i)  => q w e r t y (в столбик)

#################################################################

# text = 'До выЛетА оСтАвалОсь ещё больше тРёх чаСов'
# print(len(text))  => 42   (len)-показывает размер строки(42 символа)
# print('ещё' in text)  => True  проверка,есть ли строка'ещё' в нашем тексте
# print(text.lower())  => 'до вылета оставалось ещё больше трёх часов' (lower)-позволяет перевести все буквы нашего текста в нижний регистр
# print(text.upper())  => 'ДО ВЫЛЕТА ОСТАВАЛОСЬ ЕЩЁ БОЛЬШЕ ТРЁХ ЧАСОВ' (upper)- позволяет перевести все буквы нашего текста в верхний регистр
# print(text.replace('ещё','ЕЩЁ')) => 'До выЛетА оСтАвалОсь ЕЩЁ больше тРёх чаСов' (replace)- позволяет заменить одно слово другим(какое слово ,на какое слово)

####################################################################

# Срез  [(от):(до):(шаг)]

# text = 'до вылета оставалось ещё больше трёх часов'
# print(text[0])  =>д  выводит элемент с индексом 0
# print(text[1])  =>о  выводит элемент с индексом 1
# print(text[len(text)-1]) =>в выводит последний символ
# print(text[-1])  =>в  выводит элемент с индексом -1(последний элемент)
# print(text[-5])  =>ч  выводит элемент с индексом -5(5 элемент от конца)
# print(text[:])  =>до вылета оставалось ещё больше трёх часов  выводим полный текст    (print(text[::]))
# print(text)  =>до вылета оставалось ещё больше трёх часов   так же,выводит полный текст   (print(text[::]))
# print(text[:2])  =>до   выводит элементы с 0 по 2,не включая
# print(text[len(text)-2:])  =>ов  выводит 2 последних элемента,до индекса -2
# print(text[-2:])  =>ов  выводит 2 последних элемента,до индекса -2
# print(text[2:9])  =>вылета  выводит элементы с индекса 2 до инлекса 9,не включая(считая пробелы)
# print(text[6:-18])  =>ета оставалось ещё  выводит элементы с индекса 6 до индекса -18
# print(text[0:len(text):6])  =>детс е   выводит элементы от начала(индекс 0) до конца текста с шагом 6(каждый 6 элемент)
# print(text[::6])  =>детс е   выводит элементы от начала(индекс 0) до конца текста с шагом 6(каждый 6 элемент)
# text = text[2:9] + text[-5] + text[:2]
# print(text)   =>вылетачдо  соединяет в одну строку элементы с индексом 2 до инд 9(не вкл)+элемент с индексом -5 + элементы с 0 индекса до индекса 2 (не вкл)

#######################################################################

# Списки

# Список - это упорядоченный конечный набор элементов. Давайте разбираться, по
# сути список - это тот же самый массив, в котором можно хранить элементы любых
# типов данных.
# Как работать со списками?

# list_1 = [] # Создание пустого списка
# list_2 = list() # Создание пустого списка
# list_1 = [7, 9, 11, 13, 15, 17]

# В списках существует нумерация, которая начинается с 0, чтобы вывести первый
# элемент списка воспользуемся следующей конструкцией:
# list_1 = [7, 9, 11, 13, 15, 17]
# print(list_1[0]) # 7
# Чтобы узнать количество элементов в списке необходимо использовать функцию
# len(имя_списка):
# list_1 = [7, 9, 11, 13, 15, 17]
# print(len(list_1)) # 6
# Можно список заполнять не только при его создании, но и во время работы
# программы:

# list_1 = list() # создание пустого списка
# for i in range(5): # цикл выполнится 5 раз
# n = int(input()) # пользователь вводит целое число
# list_1.append(n) # сохранение элемента в конец списка
# 1-я итерация цикла(повторение 1): n = 12, list_1 = [12]
# 2-я итерация цикла(повторение 2): n = 7, list_1 = [12, 7]
# 3-я итерация цикла(повторение 3): n = -1, list_1 = [12, 7, -1]
# 4-я итерация цикла(повторение 4): n = 21, list_1 = [12, 7, -1, 21]
3
# 5-я итерация цикла(повторение 5): n = 0, list_1 = [12, 7, -1, 21, 0]
# print(list_1) # [12, 7, -1, 21, 0]

# Взаимодействие цикла for со списком:
# list_1 = [12, 7, -1, 21, 0]
# for i in list_1:
# print(i) # вывод каждого элемента списка
# # 1-я итерация цикла(повторение 1): i = 12
# # 2-я итерация цикла(повторение 2): i = 7
# # 3-я итерация цикла(повторение 3): i = -1
# # 4-я итерация цикла(повторение 4): i = 21
# # 5-я итерация цикла(повторение 5): i = 0
# Не забываем, что у списка есть нумерация:
# list_1 = [12, 7, -1, 21, 0]
# for i in range(len(list_1)):
# print(list_1[i]) # вывод каждого элемента списка
# 1-я итерация цикла(повторение 1): list_1[0] = 12
# 2-я итерация цикла(повторение 2): list_1[1] = 7
# 3-я итерация цикла(повторение 3): list_1[2] = -1
# 4-я итерация цикла(повторение 4): list_1[3] = 21
# 5-я итерация цикла(повторение 5): list_1[4] = 0

# Основные действия со списками:
# 1. Удаление последнего элемента списка.
# Метод pop удаляет последний элемент из списка:
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]
# 2. Удаление конкретного элемента из списка.
# Надо указать значение индекса в качестве аргумента функции pop:
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [7, -1, 21, 0]

# 3. Добавление элемента на нужную позицию.
# Функция insert — указание индекса (позиции) и значения.
# list_1 = [12, 7, -1, 21, 0]
# print(list1.insert(2, 11))  где 2-индекс,под котором будет новый элемент  11-новый элемент
# print(list1) # [12, 7, 11, -1, 21, 0]


# Срез списка


# ● Отрицательное число в индексе — счёт с конца списка
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) #[9, 10]
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1, 7]
# print(list_1[::6]) # [1, 7]


# Кортежи
# 💡 Кортеж — это неизменяемый список.
#  В случае защиты
# каких-либо данных от изменений (намеренных или случайных). Кортеж занимает
# меньше места в памяти и работают быстрее, по сравнению со списками
# t = () # создание пустого кортежа
# print(type(t)) # class <'tuple'>
# t = (1,)
# print(type(t))
# t = (1)
# print(type(t))
# t = (28, 9, 1990)
# print(type(t))
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')
# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# for e in t:
# print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support(нельзя изменять кортеж)

# Можно распаковать кортеж в независимые переменные:

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue

# Словари
# 💡 Словари — неупорядоченные коллекции произвольных объектов с
# доступом по ключу.
# В списках в качестве ключа используется индекс элемента. В словаре для
# определения элемента используется значение ключа (строка, число).
# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
# print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →

# Множества
# 💡 Множества содержат в себе уникальные элементы, не обязательно
# упорядоченные.
# Одно множество может содержать значения любых типов. Если у Вас есть два
# множества, Вы можете совершать над ними любые стандартные операции,
# например, объединение, пересечение и разность. Давайте разберем их.
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red') #  метод,добавляет заданный элемент в набор.если элемент присутствует,то не добавляет никаких элементов.
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray') # добавление
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red') # функция удаляет указанный элемент из набора и обновляет набор.
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red' если элнмнгта переданного remove не существует,генерируется исключение.
# colors.discard('red') # ok     метод удаляет элемент из набора,если элемент присутствует.возвращает none
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }   удаляет из списка всё,то есть очищает его.
# print(colors) # set()

# Операции со множествами в Python
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}  копирование
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13}  обьединение  
# i = a.intersection(b) # i = {8, 2, 5} метод находит пересечение двух и более наборов.возвращает набор,содержащий сходство между двумя и более наборами
# dl = a.difference(b) # dl = {1, 3}  возвращает установленную разницу двух наборов.разница междц наборами А и Б-набор элементов,который существует только в наборе А,но не в Б
# dr = b.difference(a) # dr = {13, 21}
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

# Неизменяемое или замороженное множество(frozenset) — множество, с которым
# не будут работать методы удаления и добавления.
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# List comprehension — это упрощенный подход к созданию списка, который
# задействует цикл for, а также инструкции if-else для определения того, что в итоге
# окажется в финальном списке.
# 1. Простая ситуация — список:
# list_1 = [exp for item in iterable]
# 2. Выборка по заданному условию:
# list_1 = [exp for item in iterable (if conditional)]
# Задача: Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
# Решение:
# 1. Создать список чисел от 1 до 100
# list_1 = []
# for i in range(1, 101):
# list_1.append(i)
# print(list_1) # [1, 2, 3,..., 100]

# Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]

# 2. Добавить условие (только чётные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
# Допустим, вы решили создать пары каждому из чисел (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,
# (100, 100)]
# Также можно умножать, делить, прибавлять, вычитать. Например, умножить
# значение на 2.
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1) # [0, 4, 8, 12, 16]

###################################################################







