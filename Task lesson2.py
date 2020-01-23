# #Task №1
#
# i = 0
# for l in range(0,6):
#     print(l, i)
#
# #Task №2
#
# sum = 0
# for i in range(10):
#     number = int(input())
#     if number == 5:
#         sum += number
# print(int(sum / 5))
#
#''' Для более красивого решения задач в стиле питона можно добавлять единицу
#if number == 5:
#   sum += 1:
#'''
#
# #Task №3
#
# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)
#
# #Task №4
#
# sum = 1
#
# for i in range(1, 11):
#     sum *= i
# print(sum)
#
# #Task №5
#
# integer_number = 2129
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10
#
# #Task №6
#
# i = 2129
# sum = 0
#
# while i > 0:
#     print(i % 10)
#     sum = sum + (i % 10) # Опять же для красоты и правильности sum += (i % 10)
#     i = i // 10
# print(sum)
#
# #Task №7
#
# i = 2129
# sum = 1
#
# while i > 0:
#     print(i % 10)
#     sum = sum * (i % 10)
#     i = i // 10
# print(sum)
#
# #Task №8
#
# integer_number = 213413
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')
#
# #Task №9
# i = 45279366174
# max = 0
#
# while i > 0:
#     if (i % 10) >= max:
#         max = (i % 10)
#     i = (i // 10)
# print(max)
#
# #Task №10
# i = 345543485234658239
# sum = 0
#
# while i > 0:
#     if i % 10 == 5:
# #        print(i % 10)
#         sum = sum + (i % 10 == 5) # Опять та же неграммотность sum += (i % 10 == 5)
#     i = i // 10
# print(sum)