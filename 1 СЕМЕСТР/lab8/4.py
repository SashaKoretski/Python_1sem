"""Корецкий ИУ7-15Б
Переставить местами столбцы с наибольшей и наименьшей
суммой элементов"""

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

    sum_stolb = [0]*N                               # Создаем список кол-ва отрицательных элементов
    for j in range(N):
        for i in range(M):
            sum_stolb[j] += A[i][j]                 # Заполняем список

    min_index = 0                                   # Индекс нужной строки
    max_index = 0
    for i in range(1,M):
        if sum_stolb[i] < sum_stolb[min_index]:     # Находим нужный столбец, запоминаем индекс
            min_index = i
        if sum_stolb[i] > sum_stolb[max_index]:
            max_index = i

    for i in range(M):                              # Меняем столбцы местами
        (A[i][max_index], A[i][min_index]) = (A[i][min_index], A[i][max_index])

    print("Получившаяся матрица: ")
    for i in range(M):
        for j in range(N):                          # Выводим получившуюся матрицу
            print(f"{A[i][j]:^+7.{5}g}", end=" ")
        print()
