"""Корецкий ИУ7-15Б
Вычисление примерного значения интеграла методом
левых прямоугольников и методом 3/8"""

import math as m
import sys


def main_function(x):   # Функция
    return x**2


def main_antiderivative(x):     # Первообразная
    return x**3/3


def rectangle_method(start, end, num, func):    # Вычисление интеграла методом левых прямоугольников
    delta_x = (end - start)/num
    moment_value = start
    integral = 0
    for _ in range(num):
        integral += delta_x*func(moment_value)
        moment_value += delta_x
    return integral


def three_eighths_method(start, end, num, func):    # Вычисление интеграла методом 3/8
    delta_x = (end - start) / num
    y_sum_no_div_three = 0
    y_sum_div_three = 0
    moment_value = start
    for i in range(1, num):
        moment_value += delta_x
        if i % 3 == 0:
            y_sum_div_three += func(moment_value)
        else:
            y_sum_no_div_three += func(moment_value)
    integral = 3/8*delta_x*(func(start) + func(end) + 3*y_sum_no_div_three + 2*y_sum_div_three)
    return integral


while True:     # Вводим значения и проверяем введенные данные на корректность
    try:
        segment_start = float(input("Введите начало отрезка интегрирования: "))
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова! ")

while True:
    try:
        segment_end = float(input("Введите конец отрезка интегрирования: "))
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова! ")

if segment_start >= segment_end:
    print("Начало отрезка должно быть меньше конца!!!")
    sys.exit()

while True:
    try:
        segment_num_1 = int(input("Введите первое количество участков разбиения: "))
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова! ")

while True:
    try:
        segment_num_2 = int(input("Введите второе количество участков разбиения: "))
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова! ")


if segment_num_1 <= 0 or segment_num_2 <= 0:
    print("Количество участков разбиения должно быть положительным!!!")
    sys.exit()

while True:
    try:
        Eps = float(input("Введите Эпсилон: "))
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова: ")

# Считаем интегралы для данного количества участков разбиения
integral_one = rectangle_method(segment_start, segment_end, segment_num_1, main_function)
integral_two = rectangle_method(segment_start, segment_end, segment_num_2, main_function)
integral_three = three_eighths_method(segment_start, segment_end, segment_num_1, main_function)
integral_four = three_eighths_method(segment_start, segment_end, segment_num_2, main_function)

# ТАБЛИЦА

print("-"*40)
print("|" + " "*12 + "|" + f"{segment_num_1:^+12.{5}g}" + "|" + f"{segment_num_2:^+12.{5}g}" + "|")
print("-"*40)
print("|   Метод 1  |" + f"{integral_one:^+12.{5}g}" + "|" + f"{integral_two:^+12.{5}g}" + "|")
print("|   Метод 2  |" + f"{integral_three:^+12.{5}g}" + "|" + f"{integral_four:^+12.{5}g}" + "|")
print("-"*40)

true_integral = main_antiderivative(segment_end) - main_antiderivative(segment_start)

accuracy_absolute_one = abs(true_integral - integral_one)   # Считаем погрешности
accuracy_for_sort = [[accuracy_absolute_one, 1]]
accuracy_relative_one = accuracy_absolute_one/true_integral
accuracy_absolute_two = abs(true_integral - integral_two)
accuracy_for_sort.append([accuracy_absolute_two, 2])
accuracy_relative_two = accuracy_absolute_two/true_integral
accuracy_absolute_three = abs(true_integral - integral_three)
accuracy_for_sort.append([accuracy_absolute_three, 3])
accuracy_relative_three = accuracy_absolute_three/true_integral
accuracy_absolute_four = abs(true_integral - integral_four)
accuracy_for_sort.append([accuracy_absolute_four, 4])
accuracy_relative_four = accuracy_absolute_four/true_integral

print()
print("Абсолютная погрешность в первом измерении равна ", end="")   # Выводим погрешности
print(f"{accuracy_absolute_one:^+12.{7}g}", end=", ")
print("a относительная " + f"{accuracy_relative_one:^+12.{5}g}!")

print("Абсолютная погрешность во втором измерении равна ", end="")
print(f"{accuracy_absolute_two:^+12.{7}g}", end=", ")
print("a относительная " + f"{accuracy_relative_two:^+12.{5}g}!")

print("Абсолютная погрешность в третьем измерении равна ", end="")
print(f"{accuracy_absolute_three:^+12.{7}g}", end=", ")
print("a относительная " + f"{accuracy_relative_three:^+12.{5}g}!")

print("Абсолютная погрешность в четвертом измерении равна ", end="")
print(f"{accuracy_absolute_four:^+12.{7}g}", end=", ")
print("a относительная " + f"{accuracy_relative_four:^+12.{5}g}!")

accuracy_for_sort.sort()    # Сортируем погрешности для определения самого точного и менее точного методов

print() # Выводим отличившиеся методы
print("Самым точным оказался ", end="")
if accuracy_for_sort[0][1] == 1 or accuracy_for_sort[0][1] == 2:
    print("метод левых прямоугольников с N = ", end="")
else:
    print("метод 3/8 c N = ", end="")

if accuracy_for_sort[0][1] == 1 or accuracy_for_sort[0][1] == 3:
    print(segment_num_1, "!")
else:
    print(segment_num_2, "!")

print("Менее точным оказался ", end="")
if accuracy_for_sort[3][1] == 1 or accuracy_for_sort[3][1] == 2:
    print("метод левых прямоугольников с N = ", end="")
    worst_method = 0
else:
    print("метод 3/8 c N = ", end="")
    worst_method = 1

if accuracy_for_sort[3][1] == 1 or accuracy_for_sort[3][1] == 3:
    print(segment_num_1, "!")
else:
    print(segment_num_2, "!")

num_of_parts = 1    # Находим кол-во участков разбиения
if worst_method == 0:
    while abs(rectangle_method(segment_start, segment_end, num_of_parts, main_function) -
              rectangle_method(segment_start, segment_end, 2*num_of_parts, main_function)) >= Eps:
        num_of_parts += 1
else:
    while abs(three_eighths_method(segment_start, segment_end, num_of_parts, main_function) -
              three_eighths_method(segment_start, segment_end, 2*num_of_parts, main_function)) >= Eps:
        num_of_parts += 1

print()
print("Для менее точного метода количество участков разбиения, ", end="")
print("для которого интеграл будет вычислен с заданной точностью равно ", num_of_parts, "!")
