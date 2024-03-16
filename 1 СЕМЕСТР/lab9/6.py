"""Корецкий ИУ7-15Б
Поэлементное перемножение матриц
сумма столбцов в итоговой матрице"""

M = int(input("Введите количество строк: "))
N = int(input("Введите количество столбцов: "))
if M < 1 or N < 1:
    print("Количество элементов должно быть положительным!!!")
else:
    A = [0]*M
    for i in range(M):
        A[i] = [0]*N                        # Заполняем матицу
        for j in range(N):
            print("Введите ", i + 1, "-й элемент ", j + 1, "-ого столбца первой матрицы: ", end="")
            A[i][j] = float(input())

    print()
    B = [0] * M
    for i in range(M):
        B[i] = [0] * N  # Заполняем матицу
        for j in range(N):
            print("Введите ", i + 1, "-й элемент ", j + 1, "-ого столбца второй матрицы: ", end="")
            B[i][j] = float(input())

    print("Данная матрица: ")
    for i in range(M):
        for j in range(N):  # Выводим матрицу
            print(f"{A[i][j]:^+7.{5}g}", end=" ")
        print()

    print()
    print("Данная матрица: ")
    for i in range(M):
        for j in range(N):  # Выводим матрицу
            print(f"{B[i][j]:^+7.{5}g}", end=" ")
        print()

    V = [0] * N
    C = [0]*M
    for i in range(M):
        C[i] = [0]*N  # Заполняем матицу
        for j in range(N):
            C[i][j] = A[i][j]*B[i][j]
            V[j] += C[i][j]

    print()
    print("Полученная матрица: ")
    for i in range(M):
        for j in range(N):  # Выводим матрицу
            print(f"{C[i][j]:^+7.{5}g}", end=" ")
        print()

    print()
    print("Сумма элементов: ")
    for j in range(N):      # Вывод суммы элементов
        print(f"{V[j]:^+7.{5}g}", end=" ")
