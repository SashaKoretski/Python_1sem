"""Корецкий ИУ7-15Б
Матрица из синусов суммы элементов из двух массивов
Определить ср ар для строк
Опр кол-во эл-в меньше ср ар"""

import math as m

d_len = int(input("Введите размер первого массива: "))
f_len = int(input("Введите размер второго массива: "))
if d_len < 0 or f_len < 0:
    print("Длины массивов должны быть положительными!!!")
else:
    D = [0]*d_len
    F = [0]*f_len

    for i in range(d_len):                              # Заполняем массивы
        print("Введите ", i + 1, "-й элемент первого массива: ", end="")
        D[i] = float(input())

    for i in range(f_len):
        print("Введите ", i + 1, "-й элемент второго массива: ", end="")
        F[i] = float(input())

    A = [0]*d_len
    for i in range(d_len):
        A[i] = [0]*f_len

    for i in range(d_len):                              # Заполняем матрицу
        for j in range(f_len):
            A[i][j] = m.sin(D[i] + F[j])

    AV = [0]*d_len                                      # Заополняем массив средних значений
    for i in range(d_len):
        poz_kol = 0
        for j in range(f_len):
            if A[i][j] > 0:
                AV[i] += A[i][j]
                poz_kol += 1
        if poz_kol > 0:
            AV[i] /= poz_kol
        else:
            AV[i] = 0

    L = [0]*d_len                                       # Заполняем массив с кол-вом элементов меньше среднего
    for i in range(d_len):
        for j in range(f_len):
            if A[i][j] < AV[i]:
                L[i] += 1


    print("Матрица" + " "*(11*f_len) + " Сред. ар."+ " "*14 + "Элементов меньше сред. ар.")
    for i in range(d_len):                              # Вывоидим матрицу и массивы
        for j in range(f_len):
            print(f"{A[i][j]:^+11.{5}g}", end=" ")
        if AV[i] > 0:
            print(f"| {AV[i]:^+24.{5}g}", end=" | ")
            print(f" {L[i]:^11.{5}g}")
        else:
            print("|Нет положительных чисел!!!|", end="")
            print(" "*7 + "-")