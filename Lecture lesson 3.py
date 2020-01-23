# # __________________________ Тип данных СТРОКА (str) _________________________
#     # Инизиализация
#
# # одинарные ковычки или двойные разницы нет, но в дальнейшем если нужно выделить символ/элемент строки а дальше ты помнишь
# temp_str = 'Марка \'Volvo\'' #Экранирование обратный бэкслеш
# #temp_str = "Марка 'Volvo'"
# print(temp_str)
#     # Обращение к символам подстроки
#
# #Вывод строки посимвольно
# for i in range(len(temp_str)):
#     print(temp_str[i])
#
# #Срезы
#
# print(temp_str[1:4])
# print(temp_str[:-4])
#
#     # Функции со строками
# print(temp_str, len(temp_str))
#
#     # Операции со строками
# temp_str2 = 'Mercedes'
#
# print(temp_str2 + temp_str) #Конкатенация
# print(temp_str2 * 2)
#
#     # Форматирование строк
#
# cars = 'Марка: {} Цена: {}'.format('Volvo', 1.5)
# print(cars)
#
# brend = 'Volvo'
# price = '1.5'
# cars = f'Марка: {brend} Цена: {price} '
#
# print(cars)
#
#     # Методы
#
# # split - метод разбиение большой строки на подстроки
#
# print(temp_str.split())
#
# cars = 'Audi, Mercedes, Lada, Suzuki'
# print(cars.split(','))
#
# #Методы форматирования строк
#
# print(cars.upper())
# print(cars.title())
# print(cars.lower())
#
# #Замена подстроки в строке
#
# email_adress = 'eMails: _mail_'
# email = 'my_email@gmail.com'
# print(email_adress.replace('_mail_', email))
#
# # __________________________ Тип данных СПИСОК (list) _________________________
#     #Инициализация (генератор)
# list_temp = []
# print(type(list_temp))
# list_temp = [1.2, 12, 'volvo', [1,2,3,4,5]]
#
# for el in list_temp:
#     print(el, type(el))
#
# # Инициализация при помощи команды list
# list_str = list('Volvo')
# print(list_str)
#
#     #Обращение к элементам списка
# for i in range(len(list_temp)):
#     print(i, ':', list_temp[i])
# for i in range(len(list_temp)):
#     print(i, ':', list_temp[i:]) #Срезы
# for i in range(len(list_temp)):
#     print(i, ':', list_temp[:i])
#
#     #Функции со списками
#
# print(len(list_temp))
#
#     #Операции со списками
# print(list_temp + list_str) # конкатенация спсика
# print(list_temp * 2)
#
#     #Методы
#
# # append - метод добавления элемента в конец списка
# intenger_list = []
# for i in range(5):
#     intenger_list.append(i)
# print(intenger_list)
# intenger_list.append(0)
# print(intenger_list)
#
# # remove - метод удаления первого встретившего из списка
#
# intenger_list.remove( 0)
# print(list)
#
# # del - функция удаления по индексу
# del intenger_list[4]
# print(intenger_list)
#
# # reverse - изсеняет порядок
#
# intenger_list.reverse()
# print(intenger_list)
#
# # sort - метод сортировки
#
# intenger_list = [1,2,8,3,5,4,8,9,4,6]
# intenger_list.sort()
# print(intenger_list)
#
# # insert - метод замены по индексу
#
# intenger_list.insert(2, 100)
# print(intenger_list)
#
#     # Обработка списков (map, filter, reduce)
#
# # map - функция которая применяется к каждому элементу списков
#
# intenger_list = [1,2,8,3,5,4,8,9,4,6]
#
# #map(function, list) ---> map ---> list(map) - каждый элемент списка стал строкой
#
# #new_intenger_list = list(map(str, intenger_list))
# #labda - функция в которой после каждого Х выполняется действие
# new_intenger_list = list(map(lambda x: x ** 2, intenger_list))
# print(new_intenger_list)
#
# # filter - фильтрация списка согласно некоторым условиям
#
# new_intenger_list = list(filter(lambda x: x < 5, intenger_list))
# print(new_intenger_list)
#
# #reduce - применяется ко всем элементам списка, возвращает некоторый 1 элемент
# from functools import reduce
#
# intenger_list = [1,2,3,4,]
#
# sum = reduce(lambda x, y: x + y, intenger_list)
# product =  reduce(lambda x, y: x * y, intenger_list)
#
# print(sum, product)
#
# # __________________________ Тип данных СЛОВАРИ (dict) _________________________
#
# '''
# Словари - похожи на списки но есть принципиальное отличие, в словарях есть ключи и значений
# Ключ - это информация по которой получаете значение.
# Различие с списками что в словорях получаем значение по каким то ключам, а в списке по индексам - это основное отличие
# Поиск и вставка значений в словорях происходит очень быстро. Словарие - эффективно реализованная конструкция '''
#
#     # Инициализация словарей
# dict_temp = {}
# print(type(dict_temp))
#
# dict_temp = {'dict1': 1, 'dict2': 2.1, 'dict3': 'name', 'dict4': [1,2,3]}
# print(dict_temp)
#
# # Метод dict.fromkeys
#
# dict_temp = dict.fromkeys(['a', 'b'], [12, 2020]) #сначала добавляются ключи 'a' и 'b', потом к обоим ключам добавляются значения
# print(dict_temp)
#
# # Метод dict
#
# dict_temp = dict(brend = 'volvo', volume_engine = 1.5)
# print(dict_temp)
#
# dict_temp = {a: a ** 2 for a in range(10)}
# print(dict_temp)
#
#     # Обращение к содержимому словарю
#
# print(dict_temp[8])
#
#     # Функции словарей
#
# # Для получения ключей словаря
#
# print(dict_temp.keys())
# print(list(dict_temp.keys())) #работают с листом
#
# # Для получения значений словарей
#
# print(dict_temp.values())
# print(list(dict_temp.values()))
#
# # Для работы с парами ключей и значений .items - возвращает кортежи
# # Кортеж - это тот же самый лист, только не изменяемый
#
# print(list(dict_temp.items()))
#
#     # Работа с элементами
#
# dict_temp[0] = 100
# dict_temp['name'] = 'Dima'
#
# print(dict_temp)
#
#     # Методы
# # .pop - удаляет ключ
#
# temp = dict_temp.pop('name')
# print(temp)
# print(dict_temp)
#
# итерирование по словарю
#
# for pair in dict_temp.items():
#     print(pair)
#
# for key, value in dict_temp.items():
#     print(key, value)
#
# for key in dict_temp.keys():
#     print(key)
#
# for value in dict_temp.values():
#     print(value)

# # __________________________ Тип данных КОРТЕЖИ (tuple) _________________________
# '''
# Кортежи - тот же самый список только не изменяемый. За счёт его не изменямости получается достичь характеристик таких
# как в скорости так и в объеме памяти. Доступ к элементам в кортеже такой же как в списках, так же доступны срезы.
# Аналогичные функции и методы. Инициализация кортежей происходит круглыми скобками ().
# '''
#
# '''
# ФУНКЦИЯ - Множества (set) - это контейнер который содержит неповторяющиеся элементы в случайном порядке.
# Множество не используют, для того чтобы по нему итерироваться. При использовании множества там где есть повторяющиеся
# элементы оно выдаст только уникальные эементы. Отличия set от frozenset заключается в том что set изменяемый тип данных,
# а frozenset не изменяемый тип данных.
# Есть операции union - объединение; intersection - пересечение; difference - разности; symmetric difference - симетрические
# разности
# '''
#      # Инициализация
# temp_tuple = (1, 2, 3)
# print(type(temp_tuple))
#
# # Можно создавать из спсика
#
# temp_list = [1, 2, 3]
# temp_tuple = tuple(temp_list)
#
# # Если возникает необходимость изменить, что- то в кортеже его форматируют в лист(список) вносят изменение и обратно
#
#      # Обращения к элементам кортежа как в списке (см раздел списки)
#
# for i in range(len(temp_tuple)):
#     print(temp_tuple[i])
#
# #temp_tuple[0] = 100 # операция присваивания выдаст ошибку так как кортеж не изменяемый
#
#      # Функции с кортежами как в списке (см. раздес списки)
#
#      # Операции с кортежами как в списке (см. раздел списки)
#
#      # Методы как в списке (см. раздел списки)
#
# # Различия в хранении памяти
#
# temp_list = [1, 2, 3]
# temp_tuple = (1, 2, 3)
#
# print(temp_list.__sizeof__()) # __sizeof__ - узнать объем занимаемой памяти
# print(temp_tuple.__sizeof__())

# # __________________________ Тип данных Множества (set) _________________________
# '''
# set обозначается фигурными скобками {}, но если в низ нет значение то тип данных будет отображаться как dict:
# temp_set = {} # dict
# temp_set = {1, 2, 3, 4} # set
# '''
#
#     # Инизиализация
# temp_set = {} # dict
# temp_set = {1, 2, 3, 4} # set
# print(type(temp_set), temp_set)
#
# temp_list = [1, 2, 1, 2, 12, 14, 15, 1, 45, 26, 45, 30]
# temp_set = set(temp_list)
#
# print(temp_set)
#
#     # Обращение к элементам множества
#
# print(100 in temp_set)
#
# for element in temp_set:
#     print(element)
#
#     # Функции с множествами - стандартные функции
#
#     # Операции с множествами
#
# # Union - объединение
# my_set_1 = set([1, 2, 3, 4, 5])
# my_set_2 = set([5, 6, 7, 8, 9])
#
# my_set_3 = my_set_1.union(my_set_2)
#
# print(my_set_3) # Мы объеденили множества, за исключением повторяющихся элементов
#
# # Difference - разности
# my_set_1 = set([1, 2, 3, 4, 5])
# my_set_2 = set([5, 6, 7, 8, 9])
#
# my_set_4 = my_set_1.difference(my_set_2)
#
# print(my_set_4) # Мы из первого множеста выкинули, те елементы которые есть во втором множестве