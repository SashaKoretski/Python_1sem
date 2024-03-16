"""Корецкий ИУ7-15Б
1) Запись чисел из файла в римской системе счисления
2) Записать числа в данном порядке"""

def file_size(file):
    sz = 0
    while True:
        lin = file.readline()
        if lin == "":
            break
        sz += 1
    return sz

def num_transform(num, f_num, file):
    if num >= 1000:
        f_num = f_num + "M"
        num -= 1000
    elif num >= 500:
        f_num = f_num + "D"
        num -= 500
    elif num >= 100:
        f_num = f_num + "C"
        num -= 100
    elif num >= 50:
        f_num = f_num + "L"
        num -= 50
    elif num >= 10:
        f_num = f_num + "X"
        num -= 10
    elif num >= 5:
        f_num = f_num + "V"
        num -= 5
    elif num >= 1:
        f_num = f_num + "I"
        num -= 1
    if num != 0:
        num_transform(num, f_num, file)
    else:
        file.write(f_num + "\n")


def main():
    f_in1 = open("in1.txt", "r")
    f_in2 = open("in2.txt", "r")
    N = file_size(f_in1)

    f_in1.close()
    f_in1 = open("in1.txt", "r")

    f_out1 = open("out1.txt", "w")
    f_out2 = open("out2.txt", "w")

    for i in range(N):
        number = int(f_in1.readline())
        print(f_in1.readline())
        num_transform(i, "", f_out1)

    f_in1.close()
    f_in2.close()
    f_out1.close()
    f_out2.close()

main()