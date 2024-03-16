"""Корецкий ИУ7-15Б
Считаем кол-во элементов в строках первой матрицы, превышающих сумму э-в в строках второй,
умножаем первую матрицу на максимальный элемент получившегося массива"""

line_one = int(input("Введите количество строк в первой матрице: "))
col_one = int(input("Введите количество столбцов в первой матрице: "))
line_two = int(input("Введите количество строк во второй матрице: "))
col_two = int(input("Введите количество столбцов во второй матрице: "))
if line_two < 0 or line_two < 0 or col_one < 0 or col_two < 0:
    print("Длина стороны матрицы должна быть положительной!!!")
elif line_two < line_one:
    print("Строк во второй матрице должно быть больше!!!")
else:
    D = [0]*line_one
    Z = [0]*line_two

    for i in range(line_one):
        D[i] = [0]*col_one                  # Вводим первую матрицу
        for j in range(col_one):
            print("Введите ", i + 1, "-й элемент ", j + 1, "-ого столбца первой матрицы: ", end="")
            D[i][j] = float(input())

    for i in range(line_two):
        Z[i] = [0]*col_two                  # Вводим вторую матрицу
        for j in range(col_two):
            print("Введите ", i + 1, "-й элемент ", j + 1, "-ого столбца второй матрицы: ", end="")
            Z[i][j] = float(input())

    print("Первая матрица: ")               # Выводим первую матрицу
    for i in range(line_one):
        for j in range(col_one):
            print(f"{D[i][j]:^+7.{5}g}", end=" ")
        print()

    print("Вторая матрица: ")
    for i in range(line_two):               # Выводим вторую матрицу
        for j in range(col_two):
            print(f"{Z[i][j]:^+7.{5}g}", end=" ")
        print()

    G = [0]*line_one
    max1 = 0
    for i in range(line_one):               # Находим G и его максимум
        line_sum = 0
        for j in range(col_two):
            line_sum += Z[i][j]
        for k in range(col_one):
            if D[i][k] > line_sum:
                G[i] += 1
        if G[i] > max1:
            max1 = G[i]

    for i in range(line_one):               # Умножаем первую матрицу
        for j in range(col_one):
            D[i][j] *= max1

    print("Первая матрица после изменения: ")  # Выводим первую матрицу
    for i in range(line_one):
        for j in range(col_one):
            print(f"{D[i][j]:^+7.{5}g}", end=" ")
        print()

    print("Массив G: ")
    for i in range(line_one):
        print(f"{G[i]:^+7.{5}g}")
