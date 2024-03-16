"""Корецкий ИУ7-15Б
База данных в бинарном файле
айди:имя_персонажа:урон:скорость_атаки"""

import struct


def menu_print():       # Вывод меню
    print("Меню программы для работы с базой данных: ")
    print("1. Выбрать файл для работы.")        # OK
    print("2. Инициализировать базу данных.")       # OK
    print("3. Вывести содержимое базы данных.")     # OK
    print("4. Добавить запись в базу данных.")      # OK
    print("5. Удалить запись из базы данных.")      # OK
    print("6. Поиск по одному полю.")       # OK
    print("7. Поиск по двум полям.")        # OK
    print("8. Печать меню.")        # OK
    print("9. Справка.")        # OK
    print("10. Выход")      # OK
    print()


def print_help():       # Вывод справки
    print("База данных состоит из имени персонажа длиной не более 13 символов, целого числа - ")
    print("урона этого персонажа, не превышающего 1000 и его скорости атаки - также целого")
    print("числа не превышающего 604.")
    print()


def file_check(file):       # Проверка файла
    if file is None:
        print("Файл не был выбран!!!\n")
        return None
    elif file[len(file) - 4: len(file)] != ".bin":
        print("Файл должен иметь расширение .bin!!!\n")
        return None
    else:
        try:
            f = open(file, "r")
            f.close()
            return file
        except FileNotFoundError:
            print("Файл не может быть открыт!!!\n")
            return None


def file_init_check(file):       # Проверка файла
    if file is None:
        print("Файл не был выбран!!!\n")
        return None
    elif file[len(file) - 4: len(file)] != ".bin":
        print("Файл должен иметь расширение .bin!!!\n")
        return None
    else:
        try:
            f = open(file, "w+")
            f.close()
            return file
        except FileNotFoundError:
            print("Файл не может быть создан!!!\n")
            return None


def file_init_check_main(file):      # Проверка файла с вводом
    if file is None:
        file = file_init_check(input("Введите имя файла: "))
    return file


def file_check_main(file):      # Проверка файла с вводом
    if file is None:
        file = file_check(input("Введите имя файла: "))
    return file


def max_id(file):       # Максимальный индекс в базе данных
    if file is None:
        return
    f = open(file, "rb")

    mi = 0
    f.seek(0, 2)
    sz = f.tell()
    f.seek(0)

    for _ in range(sz // 25):
        lin = f.read(25)
        lin = list(struct.unpack("<i13sii", lin))
        a = int(lin[0])
        if a > mi:
            mi = a
    return mi


def data_base_line_init(file, p):       # Инициализация строки в базу данных
    if file is None:
        return
    f = open(file, "ab")
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
    f.write(struct.pack("<i13sii", p, char_name.encode("utf-8"), damage, speed))
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
        data_base_line_init(file, p)


def if_data_base(file):     # Проверка, являются ли данные в файле базой данных
    if file is None:
        return
    f = open(file, "rb")
    check = 1

    f.seek(0, 2)
    sz = f.tell()
    f.seek(0)

    if sz == 0:
        return 0

    for _ in range(sz // 25):
        lin = f.read(25)
        lin = list(struct.unpack("<i13sii", lin))
        try:
            a = int(lin[0])
            n = lin[1].decode()
            d = int(lin[2])
            s = int(lin[3])
            if a < 0 or len(n) > 13 or 0 > d or 1000 < d or 0 > s or 604 < s or len(lin) != 4:
                int("a")
        except ValueError:
            check = 0
    f.close()
    return check


def print_data_base(file):      # Печать базы данных
    check = if_data_base(file)
    if file is None:
        return
    f = open(file, "rb")
    if check == 0:
        print("Файл не является базой данных!!!")
    else:
        print("-"*48)
        print("|   ID   |Имя персонажа|  Урон  |Скорость атаки|")
        print("-"*48)

        f.seek(0, 2)
        sz = f.tell()
        f.seek(0)

        for _ in range(sz // 25):
            lin = f.read(25)
            lin = list(struct.unpack("<i13sii", lin))
            a = str(lin[0])
            n = lin[1].decode().replace("\x00", "")
            d = str(lin[2])
            s = str(lin[3])
            print("|", end="")
            print(" "*((8 - len(a))//2) + a + " "*((8 - len(a) + 1)//2) + "|", end="")
            print(" " * ((13 - len(n)) // 2) + n + " " * ((13 - len(n) + 1) // 2) + "|", end="")
            print(" " * ((8 - len(d)) // 2) + d + " " * ((8 - len(d) + 1) // 2) + "|", end="")
            print(" " * ((14 - len(s)) // 2) + s + " " * ((14 - len(s) + 1) // 2) + "|")
        print("-"*48)
    f.close()


def add_to_database(file):      # Добавление строки в базу данных
    if file is None:
        return
    f = open(file, "rb+")

    f.seek(0, 2)
    sz = f.tell()
    f.seek(0)

    while True:
        try:
            add_l = int(input("Введите номер строки, на которую вы хотите поместить новую строку: "))
            print()
            if add_l <= (sz // 25):
                break
            else:
                int("a")
            break
        except ValueError:
            print("Номер был введен некорректно!!!")
            print()

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
    p = max_id(file) + 1
    f.seek(0, 2)
    f.write(struct.pack("<25s", b"0"))
    for j in range(sz//25, add_l, -1):
        f.seek(j*25 - 25)
        temp = f.read(25)
        f.seek(j*25)
        f.write(temp)
    f.seek(add_l*25)
    f.write(struct.pack("<i13sii", p, char_name.encode("utf-8"), damage, speed))
    f.close()


def delete_from_database(file):     # Удаление строки из базы данных
    if file is None:
        return
    f = open(file, "rb+")

    f.seek(0, 2)
    sz = f.tell()
    f.seek(0)

    while True:
        try:
            del_l = int(input("Введите строку для удаения: "))
            print()
            if del_l <= ((sz // 25) - 1):
                break
            else:
                int("a")
            break
        except ValueError:
            print("Номер был введен некорректно!!!")
            print()

    pointer = del_l*25
    while pointer + 25 < sz:
        f.seek(pointer + 25)
        temp = f.read(25)
        f.seek(pointer)
        f.write(temp)
        pointer += 25
    f.truncate(sz - 25)
    f.close()


def damage_check(file):     # Проверка одного поля
    check = if_data_base(file)
    if file is None:
        return
    f = open(file, "rb")
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

        f.seek(0, 2)
        sz = f.tell()
        f.seek(0)

        for _ in range(sz // 25):
            lin = f.read(25)
            lin = list(struct.unpack("<i13sii", lin))
            if int(lin[2]) >= int(min_d):
                if kol == 0:
                    print("-" * 48)
                    print("|   ID   |Имя персонажа|  Урон  |Скорость атаки|")
                    print("-" * 48)
                    kol += 1
                a = str(lin[0])
                n = lin[1].decode().replace("\x00", "")
                d = str(lin[2])
                s = str(lin[3])
                print("|", end="")
                print(" " * ((8 - len(a)) // 2) + a + " " * ((8 - len(a) + 1) // 2) + "|", end="")
                print(" " * ((13 - len(n)) // 2) + n + " " * ((13 - len(n) + 1) // 2) + "|", end="")
                print(" " * ((8 - len(d)) // 2) + d + " " * ((8 - len(d) + 1) // 2) + "|", end="")
                print(" " * ((14 - len(s)) // 2) + s + " " * ((14 - len(s) + 1) // 2) + "|")

        if kol != 0:
            print("-" * 48)
        else:
            print()
            print("Не нашлось подходящих героев!!!")
    print()
    f.close()


def dam_and_sp_check(file):     # Проверка двух полей
    check = if_data_base(file)
    if file is None:
        return
    f = open(file, "rb")
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

        f.seek(0, 2)
        sz = f.tell()
        f.seek(0)

        for _ in range(sz // 25):
            lin = f.read(25)
            lin = list(struct.unpack("<i13sii", lin))
            if int(lin[2]) >= int(min_d) and int(lin[3]) >= int(min_s):
                if kol == 0:
                    print("-" * 48)
                    print("|   ID   |Имя персонажа|  Урон  |Скорость атаки|")
                    print("-" * 48)
                    kol += 1
                a = str(lin[0])
                n = lin[1].decode().replace("\x00", "")
                d = str(lin[2])
                s = str(lin[3])
                print("|", end="")
                print(" " * ((8 - len(a)) // 2) + a + " " * ((8 - len(a) + 1) // 2) + "|", end="")
                print(" " * ((13 - len(n)) // 2) + n + " " * ((13 - len(n) + 1) // 2) + "|", end="")
                print(" " * ((8 - len(d)) // 2) + d + " " * ((8 - len(d) + 1) // 2) + "|", end="")
                print(" " * ((14 - len(s)) // 2) + s + " " * ((14 - len(s) + 1) // 2) + "|")

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
        try:        # Вводим номер пункта меню
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
        delete_from_database(file_name1)
    elif customer_choice == 6:
        file_name1 = file_check_main(file_name)
        damage_check(file_name1)
    elif customer_choice == 7:
        file_name1 = file_check_main(file_name)
        dam_and_sp_check(file_name1)
    elif customer_choice == 8:
        menu_print()
    elif customer_choice == 9:
        print_help()
    elif customer_choice == 10:
        print("До свидания!")
        break
    else:
        print("Был введен некорректный номер!!!")
        print()
