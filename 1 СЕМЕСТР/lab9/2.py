"""Корецкий ИУ7-15Б
Поворот матрицы на 90 градусов"""
M = int(input("Введите кол-во строк и столбцов: "))  # Вводим размеры матрицы
if M <= 1:
    print("Кол-во строк и столбцов должно быть положительным!!!")
else:
    A = [0]*M                                       # Создаем нулевую матрицу
    for i in range(M):
        A[i] = [0]*M

    for i in range(M):                              # Вводим элементы матрицы
        for j in range(M):
            print("Введите ", i + 1, "-й элемент ", j + 1, "-ого столбца: ", end="")
            A[i][j] = int(input())

    print("Данная матрица: ")
    for i in range(M):
        for j in range(M):                          # Выводим матрицу
            print(f"{A[i][j]:^+7.{5}g}", end=" ")
        print()

    if M % 2 == 0:
        half = M // 2
    else:
        half = (M + 1) // 2

    half = M // 2 + M % 1

    for i in range(half):
        for j in range(i, half):
            (A[i][j], A[j][M - i - 1], A[M - i - 1][M - j - 1], A[M - j - 1][i]) =\
                (A[M - j - 1][i], A[i][j], A[j][M - i - 1], A[M - i - 1][M - j - 1])

    print("Поворачиваем по часовой стрелке на 90 градусов!!!")
    for i in range(M):
        for j in range(M):                          # Выводим матрицу
            print(f"{A[i][j]:^+7.{5}g}", end=" ")
        print()

    for i in range(half):
        for j in range(i, half):
            (A[i][j], A[j][M - i - 1], A[M - i - 1][M - j - 1], A[M - j - 1][i]) =\
                (A[j][M - i - 1], A[M - i - 1][M - j - 1], A[M - j - 1][i], A[i][j])

    print("Поворачиваем против часовой стрелки на 90 градусов!!!")
    for i in range(M):
        for j in range(M):                          # Выводим матрицу
            print(f"{A[i][j]:^+7.{5}g}", end=" ")
        print()
