"""Корецкий ИУ7-15Б
Переставить местами строки с наибольшим и наименьшим количеством
отрицательных элементов"""

M = int(input("Введите кол-во строк: "))
N = int(input("Введите кол-во столбцов: "))         # Вводим размеры матрицы
if N <= 0 or M <= 0:
    print("Кол-во строк и столбцов должно быть положительным!!!")
else:
    A = [0]*M                                       # Создаем нулевую матрицу
    for i in range(M):
        A[i] = [0]*N

    for i in range(M):                              # Вводим элементы матрицы
        for j in range(N):
            print("Введите ",i + 1 ,"-й элемент ",j + 1 ,"-ого столбца: ", end="")
            A[i][j] = float(input())

    kol_otric = [0]*M                               # Создаем список кол-ва отрицательных элементов
    for i in range(M):
        for j in range(N):
            if A[i][j] <= 0:                        # Заполняем список
                kol_otric[i] += 1

    min_index = 0                                   # Индекс нужной строки
    max_index = 0
    for i in range(1,M):
        if kol_otric[i] < kol_otric[min_index]:     # Находим нужную строку, запоминаем индекс
            min_index = i
        if kol_otric[i] > kol_otric[max_index]:
            max_index = i

    for j in range(N):                              # Меняем строки местами
        (A[max_index][j], A[min_index][j]) = (A[min_index][j], A[max_index][j])

    print("Получившаяся матрица: ")
    for i in range(M):
        for j in range(N):                          # Выводим получившуюся матрицу
            print(f"{A[i][j]:^+7.{5}g}", end=" ")
        print()
