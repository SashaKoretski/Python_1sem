"""Корецкий ИУ7-15Б
Сортировка методом вставки с барьером
Исследование сортировки случайного, отсортированного и упорядоченного в обратном порядке списка"""

import sys
import time
import random as r


def insert_sort_w_bar(arr):     # Сортировка списка методом вставки с барьером
    arr = [0] + arr
    kol = 0
    n = len(arr)
    for p in range(2, n):
        arr[0] = arr[p]
        h = p
        while arr[h] < arr[h - 1]:
            arr[h], arr[h - 1] = arr[h - 1], arr[h]
            kol += 1
            h -= 1
    arr = arr[1:]
    return arr, kol


def create_random(n):       # Создание рандомного списка
    a = [0]*n
    for p in range(n):
        a[p] = r.randint(0, 10000)
    return a


def create_sorted(n):       # Создание отсортированного списка
    a = [p for p in range(n)]
    return a


def create_reverse(n):      # Создание отсортированного задом на перед списка
    a = [p for p in range(n)]
    a = a[::-1]
    return a


def number_input(wh_pr):        # Проверка ввода числа
    while True:
        try:
            print("Введите", wh_pr, end="")
            number = int(input(": "))
            break
        except ValueError:
            print("Должно быть введено целое число, попробуйте еще: ")
    return number


def wrong_num(number):      # Проверка на положительность числа
    if number <= 1:
        print("Количество элементов должно быть положительным!!!")
        sys.exit()


def time_of_sort(arr):      # Вычисление времени сортировки
    st = time.perf_counter()
    arr, kol = insert_sort_w_bar(arr)
    fin = time.perf_counter()
    return (fin - st)*1000, kol


def middle_line_print():        # Печать линии в середине таблицы
    print()
    print("|" + "-" * 13 + "|", end="")
    for _ in range(6):
        print("-" * 12 + "|", end="")
    print()


def table_print(t1, k1, t2, k2, t3, k3):        # Печать части таблицы со значениями
    t = [t1, t2, t3, k1, k2, k3]
    for p in range(3):
        print(f"{t[p]:^12.{7}g}" + "|", end="")
        print(f"{t[p + 3]:^12.{7}g}" + "|", end="")
    print()


amount_one = number_input("количество элементов в вашем списке")

wrong_num(amount_one)       # Вводим кол-во элементов в проверочном списке, проверяем на корректность

arr_one = [0]*amount_one        # Вводим проверочный список
for i in range(amount_one):
    arr_one[i] = number_input("следующий элемент списка")

print("Ваш список: ")           # Вывод списка
for i in range(amount_one):
    print(arr_one[i], end=" ")
print()

arr_one, test = insert_sort_w_bar(arr_one)
print("Отсортированный список: ")       # Вывод отсортированного списка
for i in range(amount_one):
    print(arr_one[i], end=" ")
print()

amount_n1 = number_input("количество элементов в списке")
wrong_num(amount_n1)        # Вводим кол-во элементов в следующих списках

amount_n2 = number_input("количество элементов в списке")
wrong_num(amount_n2)

amount_n3 = number_input("количество элементов в списке")
wrong_num(amount_n3)

arr_random_n1 = create_random(amount_n1)        # Генерируем нужные списки
arr_random_n2 = create_random(amount_n2)
arr_random_n3 = create_random(amount_n3)
arr_sorted_n1 = create_sorted(amount_n1)
arr_sorted_n2 = create_sorted(amount_n2)
arr_sorted_n3 = create_sorted(amount_n3)
arr_reverse_n1 = create_reverse(amount_n1)
arr_reverse_n2 = create_reverse(amount_n2)
arr_reverse_n3 = create_reverse(amount_n3)

time_list = [0]*9       # Список времен
perm_list = [0]*9       # Список списков (для удобства)
arr_list = [arr_sorted_n1, arr_sorted_n2, arr_sorted_n3, arr_random_n1, arr_random_n2,
            arr_random_n3, arr_reverse_n1, arr_reverse_n2, arr_reverse_n3]

for i in range(9):      # Считаем время и кол-во перестановок
    time_list[i], perm_list[i] = time_of_sort(arr_list[i])

# ТАБЛИЦА!!!
print("-"*93)       # Оглавление таблицы - кол-ва элементов
print("|" + " "*13 + "|" + f"{amount_n1:^25.{12}g}" + "|", end="")
print(f"{amount_n2:^25.{12}g}" + "|" + f"{amount_n3:^25.{12}g}" + "|")

print("|" + "-"*13 + "|", end="")
for _ in range(3):
    print("-"*25 + "|", end="")
print()

print("|" + " "*13 + "|", end="")       # Вторая строка таблицы
for _ in range(3):
    print(" "*2 + "Время, мс" + " "*1 + "|" + "Перестановки" + "|", end="")

middle_line_print()

print("|Упорядоченный|", end="")    # Третья строка таблицы - упорядоченный список
table_print(time_list[0], perm_list[0], time_list[1], perm_list[1], time_list[2], perm_list[2])
print("|   список    |", end="")
for _ in range(6):
    print(" "*12 + "|", end="")

middle_line_print()

print("|  Случайный  |", end="")        # Четвертая строка списка - случайный список
table_print(time_list[3], perm_list[3], time_list[4], perm_list[4], time_list[5], perm_list[5])
print("|   список    |", end="")
for _ in range(6):
    print(" "*12 + "|", end="")

middle_line_print()

print("|Упорядоченный|", end="")        # Пятая строка списка - список, упоряд-й в обратном порядке
for _ in range(6):
    print(" "*12 + "|", end="")
print()
print("| в обратном  |", end="")
table_print(time_list[6], perm_list[6], time_list[7], perm_list[7], time_list[8], perm_list[8])

print("|   порядке   |", end="")
for _ in range(6):
    print(" "*12 + "|", end="")
print()

print("-"*93)
