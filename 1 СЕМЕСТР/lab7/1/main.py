"""Корецкий ИУ7-15Б
Удаление из списка всех положительных"""

N = int(input("Введите длину вашего списка: "))     # Просим ввести длину списка
if N <= 0:
    print("Длина списка должна быть положительной!!!")     # Проверяем длину, она должна быть положительной
else:
    A = [0]*N
    for i in range(N):
        A[i] = int(input("Введите член списка: "))      # Вводим список

    j = 0
    for i in range(N):
        if A[i] <= 0:
            A[j] = A[i]       # Проверяем на положительность
            j += 1
    if j > 0:
        del A[j:N]
        print("Получившийся список: ", end="")
        for i in range(j):                      # Выводим список
            print(A[i], end=" ")
    else:
        print("В списке были только положительные значения!!!")
