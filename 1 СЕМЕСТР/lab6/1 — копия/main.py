"""Корецкий ИУ7-15Б
Добавление элемента в заданное место списка алгоритмически"""

N = int(input("Введите длину вашего списка: "))     # Просим ввести длину списка
if N <= 0:
    print("Длинна списка должна быть положительной!!!")     # Проверяем длину, она должна быть положительной
else:
    A = [None]*N
    for i in range(N):
        A[i] = int(input("Введите член списка: "))      # Вводим список

    val = int(input("Введите значение нового элемента: "))
    poz = int(input("Введите позицию нового элемента: "))
    if 0 > poz or poz > N:                             # Проверяем, коректно ли введена позиция
        print("Недопустимое значение позиции!!!")
    else:
        A.append(val)                              # Добавляем элемент в список
        for i in range(N, poz, -1):
            (A[i], A[i - 1]) = (A[i - 1], A[i])
        print("Получившийся список: ", end="")
        for i in range(N + 1):
            print(A[i], end=" ")
