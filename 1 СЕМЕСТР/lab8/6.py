"""Корецкий ИУ7-15Б
Транспонирование матрицы"""

M = int(input("Введите кол-во строк и столбцов: "))  # Вводим размеры матрицы
if M <= 1:
    print("Кол-во строк и столбцов должно быть положительным!!!")
else:
    A = [0]*M                                       # Создаем нулевую матрицу
    for i in range(M):
        A[i] = [0]*M

    for i in range(M):                              # Вводим элементы матрицы
        for j in range(M):
            print("Введите ",i + 1 ,"-й элемент ",j + 1 ,"-ого столбца: ", end="")
            A[i][j] = float(input())

    for i in range(M):
        j = i + 1                                   # Транспонируем матрицу
        while j < M:
            (A[i][j - i], A[j - i][i]) = (A[j - i][i], A[i][j - i])
            j += 1

    print("Получившаяся матрица: ")
    for i in range(M):
        for j in range(M):                          # Выводим получившуюся матрицу
            print(f"{A[i][j]:^+7.{5}g}", end=" ")
        print()
