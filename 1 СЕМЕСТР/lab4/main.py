"""Корецкий ИУ7-15Б
Уравнения y1 = sqrt(x) - 2cos(Пx/2)
          y2 = tg(0.2x + 0.3) - x**2 + 3
Вывести таблицу значений и построить график одной из них.
"""

import math as m

Pi = 3.1415

start_f = float(input("Введите начальное значение функции: "))    # Просим ввести начало, конец и шаг
end_f = float(input("Введите конечное значение функции: "))
step_f = float(input("Введите шаг функции: "))

print("-"*35)    # Выводим шапку таблицы
print("|" + " "*4 + "x" + " "*4 + "|" + " "*5 + "y1" + " "*4 + "|" + " "*5 + "y2" + " "*4 + "|")
print("-"*35)
value = start_f

while value <= end_f + step_f:
    y1_val = m.sqrt(value) - 2*m.cos(Pi*value/2)     # Считаем значения функций в точке
    y2_val = m.tan(0.2*value + 0.3) - value**2 + 3

    print(
        f"|{value:^+11.{5 if abs(value) >= 1e7 or abs(value) <= 1e-2 else 7}g}"
        f"|{y1_val:^+11.{5 if abs(y1_val) >= 1e7 or abs(y1_val) <= 1e-2 else 7}g}"
        f"|{y2_val:^+11.{5 if abs(y2_val) >= 1e7 or abs(y2_val) <= 1e-2 else 7}g}|"
    )

    value += step_f

print("-"*35)

print("\n")
