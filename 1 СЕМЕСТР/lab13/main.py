"""Корецкий ИУ7-15Б
База данных в текстовом файле
айди:имя_персонажа:урон:скорость_атаки"""


def menu_print():       # Вывод меню
    print("Меню программы для работы с базой данных: ")
    print("1. Выбрать файл для работы.")
    print("2. Инициализировать базу данных.")
    print("3. Вывести содержимое базы данных.")
    print("4. Добавить запись в конец базы данных.")
    print("5. Поиск по одному полю.")
    print("6. Поиск по двум полям.")
    print("7. Печать меню.")
    print("8. Справка.")
    print("9. Выход")
    print()


def print_help():
    print("База данных состоит из имени персонажа длиной не более 13 символов, целого числа - ")
    print("урона этого персонажа, не превышающего 1000 и его скорости атаки - также целого")
    print("числа не превышающего 604.")
    print()


def file_check(file):       # Проверка, данный файл в формате тхт и можно ли его открыть
    if file is None:
        print("Файл не был выбран!!!\n")
        return None
    elif file[len(file) - 4: len(file)] != ".txt":
        print("Файл должен иметь расширение .txt!!!\n")
        return None
    else:
        try:
            f = open(file, "r")
            f.close()
            return file
        except FileNotFoundError:
            print("Файл не может быть открыт!!!\n")
            return None


def file_check_main(file):      # Проверка на имя файла
    if file is None:
        file = file_check(input("Введите имя файла: "))
    return file


def file_init_check(file):       # Проверка, данный файл в формате тхт и можно ли его открыть
    if file is None:
        print("Файл не был выбран!!!\n")
        return None
    elif file[len(file) - 4: len(file)] != ".txt":
        print("Файл должен иметь расширение .txt!!!\n")
        return None
    else:
        try:
            f = open(file, "w+")
            f.close()
            return file
        except FileNotFoundError:
            print("Файл не может быть создан!!!\n")
            return None


def file_init_check_main(file):      # Проверка на имя файла
    if file is None:
        file = file_init_check(input("Введите имя файла: "))
    return file


def data_base_line_init(file, p):       # Инициализация строки в базе данных
    if file is None:
        return
    f = open(file, "a")
    while True:
        char_name = input("Введите имя персонажа: ")
        if char_name != "" and char_name.replace(" ", "") != "" and len(char_name) < 13:
            break
        else:
            print("Имя персонажа было введено некоректно!!!")
    while True:
        try:
            print("Введите урон", char_name, ": ", end="")
            damage = int(input())
            if 0 < damage <= 1000:
                break
            else:
                int("a")
            break
        except ValueError:
            print("Урон был введен некорректно!!!")
    while True:
        try:
            print("Введите скорость атаки", char_name, ": ", end="")
            speed = int(input())
            if 0 < speed <= 604:
                break
            else:
                int("a")
        except ValueError:
            print("Скорость атаки была введен некорректно!!!")
    print()
    f.write(str(p) + ";" + char_name + ";" + str(damage) + ";" + str(speed) + ";" + "\n")
    f.close()


def data_base_init(file):       # Инициализация базы данных
    if file is None:
        return
    f = open(file, "w")
    f.close()
    while True:
        try:
            kol = int(input("Введите количество строк: "))
            print()
            break
        except ValueError:
            print("Номер был введен некорректно!!!")
            print()
    for p in range(kol):
        data_base_line_init(file_name, p)


def if_data_base(file):     # Проверка, являются ли данные в файле базой данных
    if file is None:
        return
    f = open(file, "r")
    check = 1
    while True:
        lin = f.readline().split(";")
        if lin == [""]:
            break
        try:
            a = int(lin[0])
            n = lin[1]
            d = int(lin[2])
            s = int(lin[3])
            if a < 0 or len(n) > 13 or 0 > d or 1000 < d or 0 > s or 604 < s:
                int("a")
        except ValueError:
            check = 0
        if len(lin) != 5 or lin[-1] != "\n":
            check = 0
    f.close()
    return check


def print_data_base(file):      # Печать базы данных
    check = if_data_base(file)
    if file is None:
        return
    f = open(file, "r")
    if check == 0:
        print("Файл не является базой данных!!!")
    else:
        print("-"*48)
        print("|   ID   |Имя персонажа|  Урон  |Скорость атаки|")
        print("-"*48)
        while True:
            lin = f.readline().split(";")
            if lin == [""]:
                break
            print("|", end="")
            print(" "*((8 - len(lin[0]))//2) + lin[0] + " "*((8 - len(lin[0]) + 1)//2) + "|", end="")
            print(" " * ((13 - len(lin[1])) // 2) + lin[1] + " " * ((13 - len(lin[1]) + 1) // 2) + "|", end="")
            print(" " * ((8 - len(lin[2])) // 2) + lin[2] + " " * ((8 - len(lin[2]) + 1) // 2) + "|", end="")
            print(" " * ((14 - len(lin[3])) // 2) + lin[3] + " " * ((14 - len(lin[3]) + 1) // 2) + "|")
        print("-"*48)
    f.close()


def add_to_database(file):      # Добавление строки в базу данных
    if file is None:
        return
    f = open(file, "r")
    p = -1
    while True:
        lin = f.readline().split(";")
        if lin == [""]:
            break
        p = int(lin[0])
    f.close()
    print()
    f = open(file, "a")
    while True:
        char_name = input("Введите имя персонажа: ")
        if char_name != "" and char_name.replace(" ", "") != "" and len(char_name) < 13:
            break
        else:
            print("Имя персонажа было введено некоректно!!!")
    while True:
        try:
            print("Введите урон", char_name, ": ", end="")
            damage = int(input())
            if 0 < damage <= 1000:
                break
            else:
                int("a")
            break
        except ValueError:
            print("Урон был введен некорректно!!!")
    while True:
        try:
            print("Введите скорость атаки", char_name, ": ", end="")
            speed = int(input())
            if 0 < speed <= 604:
                break
            else:
                int("a")
        except ValueError:
            print("Скорость атаки была введен некорректно!!!")
    print()
    f.write(str(p + 1) + ";" + char_name + ";" + str(damage) + ";" + str(speed) + ";" + "\n")
    f.close()


def damage_check(file):     # Проверка одного поля
    check = if_data_base(file)
    if file is None:
        return
    f = open(file, "r")
    if check == 0:
        print("Файл не является базой данных!!!")
    else:
        while True:
            try:
                print("Введите минимальный подходящий урон: ", end="")
                min_d = int(input())
                if min_d <= 1000:
                    break
                else:
                    int("a")
                break
            except ValueError:
                print("Урон был введен некорректно!!!")
        kol = 0
        while True:
            lin = f.readline().split(";")
            if lin == [""]:
                break
            if int(lin[2]) > int(min_d):
                if kol == 0:
                    print("-" * 48)
                    print("|   ID   |Имя персонажа|  Урон  |Скорость атаки|")
                    print("-" * 48)
                    kol += 1
                print("|", end="")
                print(" " * ((8 - len(lin[0])) // 2) + lin[0] + " " * ((8 - len(lin[0]) + 1) // 2) + "|", end="")
                print(" " * ((13 - len(lin[1])) // 2) + lin[1] + " " * ((13 - len(lin[1]) + 1) // 2) + "|", end="")
                print(" " * ((8 - len(lin[2])) // 2) + lin[2] + " " * ((8 - len(lin[2]) + 1) // 2) + "|", end="")
                print(" " * ((14 - len(lin[3])) // 2) + lin[3] + " " * ((14 - len(lin[3]) + 1) // 2) + "|")
        if kol != 0:
            print("-" * 48)
        else:
            print()
            print("Не нашлось подходящих героев!!!")
    f.close()


def dam_and_sp_check(file):     # Проверка двух полей
    check = if_data_base(file)
    if file is None:
        return
    f = open(file, "r")
    if check == 0:
        print("Файл не является базой данных!!!")
    else:
        while True:
            try:
                print("Введите минимальный подходящий урон: ", end="")
                min_d = int(input())
                if min_d <= 1000:
                    break
                else:
                    int("a")
                break
            except ValueError:
                print("Урон был введен некорректно!!!")
        while True:
            try:
                print("Введите минимальную подходящую скорость атаки: ", end="")
                min_s = int(input())
                if min_s <= 604:
                    break
                else:
                    int("a")
                break
            except ValueError:
                print("Скорость атаки была введена некорректно!!!")
        kol = 0
        while True:
            lin = f.readline().split(";")
            if lin == [""]:
                break
            if int(lin[2]) > int(min_d) and int(lin[3]) > int(min_s):
                if kol == 0:
                    print("-" * 48)
                    print("|   ID   |Имя персонажа|  Урон  |Скорость атаки|")
                    print("-" * 48)
                    kol += 1
                print("|", end="")
                print(" " * ((8 - len(lin[0])) // 2) + lin[0] + " " * ((8 - len(lin[0]) + 1) // 2) + "|", end="")
                print(" " * ((13 - len(lin[1])) // 2) + lin[1] + " " * ((13 - len(lin[1]) + 1) // 2) + "|", end="")
                print(" " * ((8 - len(lin[2])) // 2) + lin[2] + " " * ((8 - len(lin[2]) + 1) // 2) + "|", end="")
                print(" " * ((14 - len(lin[3])) // 2) + lin[3] + " " * ((14 - len(lin[3]) + 1) // 2) + "|")
        if kol != 0:
            print("-" * 48)
        else:
            print()
            print("Не нашлось подходящих героев!!!")
    print()
    f.close()


menu_print()
file_name = None
while True:
    while True:
        try:        # Выбор пункта
            customer_choice = int(input("Введите номер пункта: "))
            print()
            break
        except ValueError:
            print("Номер был введен некорректно!!!")
            print()
    if customer_choice == 1:
        file_name = file_check_main(file_name)
    elif customer_choice == 2:
        file_name1 = file_init_check_main(file_name)
        data_base_init(file_name1)
    elif customer_choice == 3:
        file_name1 = file_check_main(file_name)
        print_data_base(file_name1)
    elif customer_choice == 4:
        file_name1 = file_check_main(file_name)
        add_to_database(file_name1)
    elif customer_choice == 5:
        file_name1 = file_check_main(file_name)
        damage_check(file_name1)
    elif customer_choice == 6:
        file_name1 = file_check_main(file_name)
        dam_and_sp_check(file_name1)
    elif customer_choice == 7:
        menu_print()
    elif customer_choice == 8:
        print_help()
    elif customer_choice == 9:
        print("До свидания!")
        break
    else:
        print("Был введен некорректный номер!!!")
        print()
