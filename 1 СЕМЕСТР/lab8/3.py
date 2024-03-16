"""Корецкий ИУ7-15Б
Столбец с минимальным кол-вом чисел, являющимися степенями двойки"""

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

    kol_step = [0]*N                                # Создаем список кол-ва четных элементов
    for j in range(N):
        for i in range(M):
            is_step = 0
            step = 1
            if A[i][j] >= 1:
                while step <= A[i][j]:              # Проверяем, является ли число степенью двойки
                    if step == A[i][j]:
                        is_step = 1
                    step *= 2
            elif 0 < A[i][j] < 1:
                while step >= A[i][j]:
                    if step == A[i][j]:
                        is_step = 1
                    step /= 2
            if is_step == 1:
                kol_step[j] += 1

    min_index = 0                                   # Индекс нужной строки
    for j in range(1,N):
        if kol_step[j] < kol_step[min_index]:       # Находим нужную строку, запоминаем индекс
            min_index = j

    print("Столбец с минимальным кол-вом чисел, являющимися степенями двойки: ")
    for i in range(M):                              # Выводим нужную строку
        print(f"{A[i][min_index]:^+7.{5}g}")
