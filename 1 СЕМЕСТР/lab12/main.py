"""Корецкий ИУ7-15Б
Текстовый процессор"""


def menu_print(full):       # Вывод меню
    if full == 1:
        print("Меню текстового процессора: ")
        print("1. Выровнять текст по левому краю.")     # OK
        print("2. Выровнять текст по правому краю.")        # OK
        print("3. Выровнять текст по ширине.")      # OK
        print("4. Удаление всех возможных вхождений слова.")        # OK
        print("5. Замена одного слова другим во всем тексте.")      # OK
        print("6. Сложение и вычитание целых чисел внутри текста.")     # OK
        print("7. Удаление самого длинного по вхождению слов предложения.")     # OK
        print("8. Печать текста.")      # OK
    print("9. Печать меню.")        # OK
    print("10. Выход")      # OK
    print()


def len_text_string(text, arr):     # Считаем длины строк
    for p in range(len(text)):
        arr[p] = len(text[p])


def max_len_count(text):     # Находим длину самой длинной строки
    arr = [0] * len(text)
    len_text_string(text, arr)
    max_len = 0
    max_ind = 0
    for p in range(len(arr)):
        if max_len < arr[p]:
            max_len = arr[p]
            max_ind = p
    return arr[max_ind]


def space_count(text, arr):        # Считаем количество пробелов в строках
    for p in range(len(text)):
        space_amount = 0
        b = 0
        while text[p][b] == " ":
            b += 1
        for k in range(b + 1, len(text[p])):
            if text[p][k] == " ":
                space_amount += 1
        arr[p] = space_amount


def space_destroyer(text):      # Убирает пробелы между словами (кроме одного)
    for p in range(len(text)):
        while "  " in text[p]:
            text[p] = text[p].replace("  ", " ")


def last_sp_destroyer(text):        # Убирает последний пробел
    for p in range(len(text)):
        if text[p][-1] == " ":
            text[p] = text[p][0: len(text[p]) - 1]


def text_print(text):       # Выводим текст
    print()
    for p in range(len(text)):
        print(text[p])
    print()
    print()


def text_right(text):      # Выравнивание текста по правому краю
    last_sp_destroyer(text)
    space_destroyer(text)
    max_len = max_len_count(text)
    for p in range(len(text)):
        text[p] = " "*(max_len - len(text[p])) + text[p]


def text_left(text):        # Выравниваем текст по левому краю
    space_destroyer(text)
    b = 0
    for p in range(len(text)):
        for k in range(len(text[p])):
            if text[p][k] != " ":
                b = k
                break
        le = len(text[p])
        text[p] = text[p][b:le]


def text_middle(text):      # Выравнивание текста по шинине
    text_left(text)
    last_sp_destroyer(text)
    max_len = max_len_count(text)
    for p in range(len(text)):
        kol = 1
        while len(text[p]) < max_len:
            text[p] = text[p].replace(" "*kol, " "*(kol + 1))
        for _ in range(max_len, len(text[p])):
            text[p] = text[p].replace(" " * (kol + 1), " " * kol, 1)


def eq_end(el):     # Проверка, является ли элемент значением, которое может находится в конце слова вплолтную
    if el == "." or el == "!" or el == "?" or el == ")" or el == "%" or el == "$" or el == ":" or el == ";":
        return True
    if el == "," or el == "\'" or el == "\"":
        return True
    return False


def eq_beg(el):     # Проверка, является ли элемент значением, которое может находится в начале слова вплолтную
    if el == "(" or el == "\'" or el == "\"":
        return True
    return False


# def word_change(text, word1, word2):        # Замена всех вхождений слова на другое слово
#     joined_text = []
#     for p in range(len(text)):
#         joined_text += text[p].split()
#     for p in range(len(joined_text)):
#         word_index = joined_text[p].lower().find(word1.lower())
#         word_index = int(word_index)
#         if word_index == -1:
#             continue
#         if len(joined_text[p]) - len(word1) > 2:
#             continue
#         if word_index == 0:
#             if len(joined_text[p]) == len(word1):
#                 joined_text[p] = joined_text[p].lower().replace(word1, word2)
#             else:
#                 if eq_end(joined_text[p][-1]):
#                     joined_text[p] = joined_text[p].lower().replace(word1, word2)
#                 else:
#                     continue
#         elif len(joined_text[p]) - len(word1) == 1:
#             if eq_beg(joined_text[p][0]):
#                 joined_text[p] = joined_text[p].replace(word1, word2)
#             else:
#                 continue
#         else:
#             if eq_beg(joined_text[p][0]) and eq_end(joined_text[p][-1]):
#                 joined_text[p] = joined_text[p].replace(word1, word2)
#             else:
#                 continue
#     text_new = []
#     k = 0
#     max_len = max_len_count(text)
#     while k < len(joined_text):
#         lin = ""
#         while len(lin) < max_len and k < len(joined_text):
#             lin += joined_text[k] + " "
#             k += 1
#         text_new.append(lin)
#     for p in range(len(text_new)):
#         text[p] = text_new[p]
#     for _ in range(len(text) - len(text_new)):
#         text.pop()


def word_change(text, word1, word2):        # Замена всех вхождений слова на другое слово
    for p in range(len(text)):
        our_line = text[p].split()
        text[p] = ""
        for k in range(len(our_line)):
            word_index = our_line[k].lower().find(word1.lower())
            word_index = int(word_index)
            if word_index == -1:
                text[p] += our_line[k]
                text[p] += " "
                continue
            if len(our_line[k]) - len(word1) > 2:
                text[p] += our_line[k]
                text[p] += " "
                continue
            if word_index == 0:
                if len(our_line[k]) == len(word1):
                    our_line[k] = our_line[k].lower().replace(word1, word2)
                else:
                    if eq_end(our_line[k][-1]):
                        our_line[k] = our_line[k].lower().replace(word1, word2)
                    else:
                        text[p] += our_line[k]
                        text[p] += " "
                        continue
            elif len(our_line[k]) - len(word1) == 1:
                if eq_beg(our_line[k][0]):
                    our_line[k] = our_line[k].replace(word1, word2)
                else:
                    text[p] += our_line[k]
                    text[p] += " "
                    continue
            else:
                if eq_beg(our_line[k][0]) and eq_end(our_line[k][-1]):
                    our_line[k] = our_line[k].replace(word1, word2)
                else:
                    text[p] += our_line[k]
                    continue
            text[p] += our_line[k]
            text[p] += " "


# def word_change(text, word1, word2):        # Замена всех вхождений слова на другое слово
#     reg_b = "(?i)(\W|^)"
#     reg_e = "(\W|$)"
#     for p in range(len(text)):
#         b = text[p].split()
#         text[p] = ""
#         for k in range(len(b)):
#             if re.search(reg_b + word1 + reg_e, b[k]):
#                 b[k] = b[k].lower().replace(word1, word2)
#             if k != len(b) - 1:
#                 b[k] += " "
#             text[p] += b[k]


def word_del(text, word):       # Удаление всех вхождений слов
    word_change(text, word, "")


def align_text(text, ali):      # Определяет, какое выравнивание было использовано до изменения текста
    if ali == 1:
        text_left(text)
    elif ali == 2:
        text_right(text)
    else:
        text_middle(text)


def is_number(word):        # Проверяет, является ли данные в строке целым числом
    try:
        int(word)
    except ValueError:
        return False
    return True


def plus_and_minus(text):       # Решает все примеры на сложение и вычитание в тексте
    joined_text = []
    new_text = []
    for p in range(len(text)):
        joined_text += text[p].split()
    pl_or_mn = "pl"
    next_fl = 1
    for p in range(len(joined_text)):
        next_fl += 1
        check = 0
        if joined_text[p].find("+") != -1:
            pl_or_mn = "pl"
            check = 1
        elif joined_text[p].find("-") != -1:
            pl_or_mn = "mn"
            check = 1
        if check == 1:      # Если в элементе есть + или -
            if len(joined_text[p]) == 1:        # Когда только знак
                if p == 0 or p == (len(joined_text) - 1):
                    continue
                else:
                    if is_number(joined_text[p - 1]) and is_number(joined_text[p + 1]):
                        if pl_or_mn == "pl":
                            the_sum = int(joined_text[p - 1]) + int(joined_text[p + 1])
                        else:
                            the_sum = int(joined_text[p - 1]) - int(joined_text[p + 1])
                        new_text[-1] = str(the_sum)
                        next_fl = -1
                    else:
                        new_text.append(str(joined_text[p]))
            else:
                if joined_text[p][-1] == "+" or joined_text[p][-1] == "-":      # Когда знак в конце
                    if p == len(joined_text) - 1:
                        new_text.append(joined_text[p])
                        break
                    elif is_number(joined_text[p][:-1]) and is_number(joined_text[p + 1]):
                        if pl_or_mn == "pl":
                            the_sum = int(joined_text[p][:-1]) + int(joined_text[p + 1])
                        else:
                            the_sum = int(joined_text[p][:-1]) - int(joined_text[p + 1])
                        new_text.append(str(the_sum))
                        next_fl = -1
                    else:
                        new_text.append(str(joined_text[p]))
                elif joined_text[p][0] == "+" or joined_text[p][0] == "-":      # Когда знак в начале
                    if p == 0:
                        new_text.append(joined_text[p])
                        continue
                    elif is_number(joined_text[p][1:]) and is_number(joined_text[p - 1]):
                        if pl_or_mn == "pl":
                            the_sum = int(joined_text[p][1:]) + int(joined_text[p - 1])
                        else:
                            the_sum = - int(joined_text[p][1:]) + int(joined_text[p - 1])
                        new_text[-1] = str(the_sum)
                    else:
                        new_text.append(str(joined_text[p]))
                else:
                    if pl_or_mn == "pl":
                        a = joined_text[p].split("+")
                        if is_number(a[0]) and is_number(a[1]):
                            the_sum = int(a[0]) + int(a[1])
                        else:
                            continue
                    else:
                        a = joined_text[p].split("-")
                        if is_number(a[0]) and is_number(a[1]):
                            the_sum = int(a[0]) - int(a[1])
                        else:
                            continue
                    new_text.append(str(the_sum))
        elif next_fl != 0:
            new_text.append(joined_text[p])
    max_len = max_len_count(text)
    text_new = []
    k = 0
    while k < len(new_text):
        lin = ""
        while len(lin) < max_len and k < len(new_text):
            lin += new_text[k] + " "
            k += 1
        text_new.append(lin)
    for p in range(len(text_new)):
        text[p] = text_new[p]
    for _ in range(len(text) - len(text_new)):
        text.pop()


def the_biggest_sent_delete(text):      # Удаляет самое длинное предложение
    max_index = 0
    index_now = 0
    max_len = 0
    len_now = 0
    for p in range(len(text)):
        joined_text = text[p].split()
        for k in range(len(joined_text)):
            len_now += 1
            if joined_text[k][-1] == "." or joined_text[k][-1] == "!" or joined_text[k][-1] == "?":
                index_now += 1
                if len_now > max_len:
                    max_len = len_now
                    max_index = index_now
                len_now = 0
    if index_now == 1:
        print("Остальсь одно предложение!!!")
        return
    index_now = 0
    ind = 0
    sto = 0
    for p in range(len(text)):
        joined_text = text[p].split()
        for k in range(len(joined_text)):
            if joined_text[k][-1] == "." or joined_text[k][-1] == "!" or joined_text[k][-1] == "?":
                index_now += 1
                if index_now == max_index:
                    ind = k
                    sto = p

    joined_text = text[sto].split()
    joined_text.pop(ind)
    if ind == 0:
        text[sto] = ""
        for u in range(1, len(joined_text)):
            text[sto] += joined_text[u] + " "
        if sto != 0:
            sto -= 1
            joined_text = text[sto].split()
            ind = len(joined_text) - 1
    else:
        ind -= 1

    check = 0
    while joined_text[ind][-1] != "." and joined_text[ind][-1] != "!" and joined_text[ind][-1] != "?":
        if ind == 0:
            text[sto] = ""
            for u in range(1, len(joined_text)):
                text[sto] += joined_text[u] + " "
            if sto != 0:
                sto -= 1
                joined_text = text[sto].split()
                ind = len(joined_text) - 1
            else:
                check = 1
                break
        else:
            joined_text.pop(ind)
            ind -= 1

    if check == 0:
        text[sto] = ""
        for u in range(len(joined_text)):
            text[sto] += joined_text[u] + " "

# def the_biggest_sent_delete(text):      # Удаляет самое длинное предложение
#     max_len = max_len_count(text)
#     joined_text = []
#     for p in range(len(text)):
#         joined_text += text[p].split()
#     b_sen = 0
#     e_sen = 0
#     b_now = 0
#     big_size = 0
#     sent_kol = 0
#     for p in range(len(joined_text)):
#         if joined_text[p][-1] == "." or joined_text[p][-1] == "!" or joined_text[p][-1] == "?":
#             sent_kol += 1
#             if p - b_now > big_size:
#                 b_sen = e_sen
#                 big_size = p - e_sen
#                 e_sen = p
#                 b_now = b_sen
#             else:
#                 b_now = p
#     if sent_kol == 1:
#         print()
#         print("Осталось только одно предложение!!!")
#         print()
#     else:
#         for _ in range(e_sen - b_sen):
#             joined_text.pop(b_sen + 1)
#         text_new = []
#         k = 0
#         while k < len(joined_text):
#             lin = ""
#             while len(lin) < max_len and k < len(joined_text):
#                 lin += joined_text[k] + " "
#                 k += 1
#             text_new.append(lin)
#         for p in range(len(text_new)):
#             text[p] = text_new[p]
#         for _ in range(len(text) - len(text_new)):
#             text.pop()
#         print()
#         print("Самое длинное предлложение удалено!")
#         print()


def main(main_text):
    is_full = 1
    which_align = 1
    while True:
        menu_print(is_full)
        is_full = 0
        while True:
            try:
                customer_choice = int(input("Введите номер пункта: "))
                break
            except ValueError:
                print("Номер был введен некорректно!!!")
                print()
        if customer_choice == 1:
            text_left(main_text)
            which_align = 1
            print()
            print("Текст выровнялся по левому краю!")
            print()
            text_print(main_text)
        elif customer_choice == 2:
            text_right(main_text)
            which_align = 2
            print()
            print("Текст выровнялся по правому краю!")
            print()
            text_print(main_text)
        elif customer_choice == 3:
            text_middle(main_text)
            which_align = 3
            print()
            print("Текст выровнялся по ширине!")
            print()
            text_print(main_text)
        elif customer_choice == 4:
            word_for_del = input("Введите слово, все вхождения которого вы хотите удалить: ")
            if word_for_del == "":
                print()
                print("Должно быть введено слово!")
                print()
            else:
                word_del(main_text, word_for_del)
                align_text(main_text, which_align)
                print()
                print("Все вхождения данного слова удалены!")
                print()
                text_print(main_text)
        elif customer_choice == 5:
            word_one = input("Введите слово, которое хотите заменить: ")
            if word_one == "":
                print()
                print("Должно быть введено слово!")
                print()
            else:
                word_two = input("Введите слово, на которое хотите заменить: ")
                word_change(main_text, word_one, word_two)
                align_text(main_text, which_align)
                print()
                print("Все вхождения данного слова заменены!")
                print()
                text_print(main_text)
        elif customer_choice == 6:
            plus_and_minus(main_text)
            align_text(main_text, which_align)
            text_print(main_text)
        elif customer_choice == 7:
            the_biggest_sent_delete(main_text)
            align_text(main_text, which_align)
            text_print(main_text)
        elif customer_choice == 8:
            text_print(main_text)
        elif customer_choice == 9:
            is_full = 1
        elif customer_choice == 10:
            print("До свидания!")
            break
        else:
            print("Был введен некорректный номер!!!")
            print()


m_text = list(["Разрывая конверт, он уже? подсчитал мысленно все "])
m_text.append("свои долги. 3 - 999 доллара 85 Уже, центов в бакалейную ")
m_text.append("лавку; 4 — мяснику; 2+3 булочнику; за овощи — ")
m_text.append("and end")
m_text.append("5+ 14 ,85. Далее, за комнату 1 - 2 ,50, за месяц вперед — ")
m_text.append("2,50; за двухмесячный прокат уЖе машинки — 8, за уже ")
m_text.append("месяц вперед — 4; всего 31,85. Кроме того, надо ")
m_text.append("выкупить вещи из ломбарда: часы — 5,50; пальто — 5,50, велосипед — 3+")
m_text.append("7 ,75; костюм — 5,50 (из 60 % — но не все ли равно!). Общий итог — ")
m_text.append("56,10. Эта сумма словно была выписана перед ним в воздухе светящимися ")
m_text.append("цифрами. Остаток в 43 доллара 90 центов представлял ")
m_text.append("необычайное богатство, неужели принимая во внимание, что будет ")
m_text.append("уплачено вперед и за комнату и за машинку.")

n_text = list(["1 2 3"])
n_text.append("4. 5 6! 7")
n_text.append("8 9 0 1?")

main(m_text)
