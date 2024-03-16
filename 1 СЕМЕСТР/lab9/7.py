"""Корецкий ИУ7-15Б
Срез трехмерного массива"""

M = int(input("Введите количество строк: "))
N = int(input("Введите количество столбцов: "))
K = int(input("Введите глубину массива: "))
if M < 1 or N < 1 or K < 1:
    print("Количество элементов должно быть положительным!!!")
else:
    A = [0] * M
    for i in range(M):
        A[i] = [0] * N  # Заполняем матицу
        for j in range(N):
            A[i][j] = [0]*K
            for t in range(K):
                print("Введите ", i + 1, "-й элемент ", j + 1, end="")
                print("-ого столбца", t + 1,  "-й глубины: ", end="")
                A[i][j][t] = float(input())

    index = int(input("Введите индекс среза: "))
    if index > N or index <= 0:
        print("Индекс не подходит!!!")
    else:
        print(index, "-й срез: ")
        for i in range(M):
                for t in range(K):
                    print(f"{A[i][index - 1][t]:^+7.{5}g}", end=" ")
                print()
