"""Корецкий Иу7-15Б
Замена всех гласных английских букв в матрице на точки"""

import string as s

M = int(input("Введите количество строк: "))
N = int(input("Введите количествоо столбцов: "))
if M < 1 or N < 1:
    print("Количество элементов должно быть положительным!!!")
else:
    A = ["0"]*M
    error = 0
    for i in range(M):
        A[i] = ["0"]*N
        for j in range(N):                  # Заполняем матрицу
            print("Введите ", i + 1, "-й элемент ", j + 1, "-ого столбца второй матрицы: ", end="")
            A[i][j] = input()
            if len(A[i][j]) != 1:
                print("Строка должна содержать один символ!!!")
                error = 1
                break

    if error == 0:
        print("Mатрица: ")  # Выводим матрицу
        for i in range(M):
            for j in range(N):
                print(A[i][j], end=" ")
            print()

        for i in range(M):                      # Меняем гласные на точки
            for j in range(N):
                if A[i][j] == "e" or A[i][j] == "E" or A[i][j] == "y" or A[i][j] == "Y" or A[i][j] == "u" or \
                    A[i][j] == "U" or A[i][j] == "i" or A[i][j] == "I" or A[i][j] == "o" or A[i][j] == "O" or \
                        A[i][j] == "a" or A[i][j] == "A":
                    A[i][j] = "."

        print()
        print("Mатрица с замененными элементами: ")  # Выводим матрицу
        for i in range(M):
            for j in range(N):
                print(A[i][j], end=" ")
            print()
