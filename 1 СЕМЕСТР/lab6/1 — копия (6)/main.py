"""Корецкий ИУ7-15Б
Меняем местами минимальный чётный и максимальный нечётный"""

N = int(input("Введите длину вашего списка: "))     # Просим ввести длину списка
if N <= 0:
    print("Длинна списка должна быть положительной!!!")     # Проверяем длину, она должна быть положительной
else:
    A = [None]*N
    chet = 0
    for i in range(N):
        A[i] = int(input("Введите член списка: "))      # Вводим список
        if A[i] % 2 == 0:
            chet += 1

    if chet == 0:                               # Проверка, есть ли четные и нечетные числа
        print("В списке нет четных чисел!!!")
    elif chet == N:
        print("В списке нет нечетных чисел!!!")
    else:
        min_ch = -1
        max_nch = -1
        for i in range(N):                  # Ищем минимальный чётный и максимальный нечётный
            if A[i] % 2 == 0:
                if min_ch == -1:
                    min_ch = i
                elif A[min_ch] > A[i]:
                    min_ch = i
            elif A[i] % 2 == 1:
                if max_nch == -1:
                    max_nch = i
                elif A[max_nch] < A[i]:
                    max_nch = i
        (A[min_ch], A[max_nch]) = (A[max_nch], A[min_ch])       # Меняем их местами
        print("Получившийся список: ", end="")
        for i in range(N):
            print(A[i], end=" ")            # Вывод списка
