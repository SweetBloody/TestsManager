from test_process import get_file_name_for_args, get_double_file_name_for_args


# Ввод пути в файловой системе
def input_path(message):
    path = input(message)
    if len(path) != 0 and path[len(path) - 1] != "\\":
        path += "\\"
    return path


# Ввод числа
def input_number(message):
    number = input(message)
    try:
        number = int(number)
    except ValueError:
        print("Введите число!\n")
    return number


# Ввод типа теста
def input_test_type():
    num = 0
    while num != 1 and num != 2:
        num = input_number("Введите тип теста (1 - 'pos' или 2 - 'neg'):\n")
    if num == 1:
        type = "pos"
    else:
        type = "neg"
    return type


# Ввод количества тестов
def input_tests_amount(mode):
    if mode == "pos":
        amount = input_number("Введите количество позитивных тестов:\n")
    else:
        amount = input_number("Введите количество негативных тестов:\n")
    return amount


# Ввод аргументов командной строки
def input_arguments():
    args = input("Введите аргументы командной строки:\n")
    return args


# Ввод количества входных файлов
def input_in_file_mode():
    in_file_mode = input_number("Введите количество входных файлов:\n")
    return in_file_mode


# Чтение аргументов из файла настроек
def input_arguments_from_file(file):
    string = file.readline()
    if len(string) != 0 and string[len(string) - 1] == '\n':
        string = string[:-1]
    return string


# Запись аргументов в файл
def print_args_to_file(file_name, args, mode, index, out_file_mode, in_file_mode):
    file = open(file_name, 'w')
    in_file_2 = ""
    if in_file_mode == 1:
        in_file_1 = get_file_name_for_args(mode, index, "in")
        in_file = in_file_1
    else:
        in_file_1 = get_double_file_name_for_args(mode, index, "in", 1)
        in_file_2 = get_double_file_name_for_args(mode, index, "in", 2)
        in_file = in_file_1 + " " + in_file_2
    out_file = get_file_name_for_args(mode, index, "out")
    if out_file_mode == 1:
        file.write(in_file + " " + out_file + " " + args + "\n")
    else:
        file.write(in_file + " " + args + '\n')
    file.close()


# Ввод данных
def input_data(message):
    print(message)
    text = []
    while True:
        string = input()
        if string == "^":
            break
        text.append(string)
    return text


# Чтение данных из файла настроек
def input_data_from_file(file):
    text = []
    while True:
        string = file.readline()
        if string == "-----\n" or string == "-----":
            break
        text.append(string)
    return text


# Запись данных в файл
def print_data_to_file(file_name, text, mode):
    file = open(file_name, 'w')
    if mode == 1:
        for string in text:
            file.write(string)
    else:
        for string in text:
            file.write(string + '\n')
    file.close()


# Информация о добавлении в параметры выходного файла
def is_out_file():
    print("\nУкажите, нужно ли в параметрах командной строки\n"
          "указывать выходной файл (1 - да / 2 - нет).")
    choice = input_number("Ваш выбор:\n")
    return choice


# Печать таблицы меню
def print_manual_menu_table():
    print("┌", "─" * 50, "┐")
    print("│", "  MENU", " " * 43, "│")
    print("│", "  1. Ввести путь для сохренения тестов            ", "│")
    print("│", "  2. Ввести путь нахождения исполнительного файла ", "│")
    print("│", "  3. Ввести позитивные тесты                      ", "│")
    print("│", "  4. Ввести негативные тесты                      ", "│")
    print("│", "  5. Изменить/создать отдельный тест              ", "│")
    print("│", "  6. Выбор количества входных файлов              ", "│")
    print("│", " -1. Важная информация о программе                ", "│")
    print("│", "  0. Выход                                        ", "│")
    print("└", "─" * 50, "┘")


# Обработка меню
def manual_menu():
    choice = ""
    print_manual_menu_table()
    while type(choice) == str or choice < -1 or choice > 6:
        choice = input_number("Введите необходимый пункт меню (от -1 до 6):\n")
    return choice


# Печать таблицы меню
def print_file_menu_table():
    print("┌", "─" * 50, "┐")
    print("│", "  MENU", " " * 43, "│")
    print("│", "  1. Ввести путь для сохранения тестов            ", "│")
    print("│", "  2. Ввести путь нахождения исполнительного файла ", "│")
    print("│", "  3. Создать позитивные тесты                     ", "│")
    print("│", "  4. Создать негативные тесты                     ", "│")
    print("│", "  5. Выбор количества входных файлов              ", "│")
    print("│", " -1. Важная информация о программе                ", "│")
    print("│", " -2. Создать примеры файлов настроек              ", "│")
    print("│", "  0. Выход                                        ", "│")
    print("└", "─" * 50, "┘")


# Обработка меню
def file_menu():
    choice = ""
    print_file_menu_table()
    while type(choice) == str or choice < -2 or choice > 5:
        choice = input_number("Введите необходимый пункт меню (от -2 до 5):\n")
    return choice


# Вывод информации о программе
def info(run_mode):
    if run_mode == 0:
        print("TestsManager\n")
        print("Данная программа создана для упрощения создания тестов для\n"
              "лабораторных работ по си.\n\n"
              "ВАЖНЫЕ МОМЕНТЫ:\n"
              " - если вы не указываете путь папки, в которую вы хотите сохранить\n"
              "   тесты, то они сохранятся в папку func_tests, которая создастся в\n"
              "   той же директории, в которой находится исполняемый файл\n"
              "   программы TestsManager;\n"
              " - если вы не указываете путь, по которому находится файл программы,\n"
              "   для которой создаются тесты, то нужно поместить этот файл в\n"
              "   директорию программы TestsManager;\n"
              " - исполняемый файл программы, для которой создаются тесты, должен\n"
              "   называться app.exe;\n\n"
              "Пример директории для корректной работы программы (если вы не\n"
              "указываете пути для исполняемого файла вашей программы и папки\n"
              "для сохранения тестов):\n"
              "/some_dir/\n"
              "    TestsManager.exe\n"
              "    app.exe\n"
              "    [/func_tests/]\n")
    elif run_mode == 1:
        print("Важная информация для этого режима работы программы:\n"
              " - необходимо создать два файла настроек (файлы с данными для тестов):\n"
              "     * tests.txt      - файл с входными данными, окончанием ввода данных\n"
              "                        является строка '-----' (5 символов);\n"
              "     * tests_args.txt - файл с аргументами командной строки, в каждой\n"
              "                        строке написаны аргументы для соответствующего\n"
              "                        теста (без названия входных\\выходных файлов)\n"
              " - для лучшего понимания, как создать правильные файлы настроек,\n"
              "   запустите пункт меню '-2'\n\n"
              "Пример директории для корректной работы программы (если вы не\n"
              "указываете пути для исполняемого файла вашей программы и папки\n"
              "для сохранения тестов):\n"
              "/some_dir/\n"
              "    TestsManager.exe\n"
              "    app.exe\n"
              "    tests.txt\n"
              "    tests_args.txt\n"
              "    [/func_tests/]\n")
    else:
        print("Важная информация для этого режима работы программы:\n"
              " - чтобы завершить ввод данных для входного файла нужно последней\n"
              "   строкой ввести символ '^'\n\n"
              "Пример директории для корректной работы программы (если вы не\n"
              "указываете пути для исполняемого файла вашей программы и папки\n"
              "для сохранения тестов):\n"
              "/some_dir/\n"
              "    TestsManager.exe\n"
              "    app.exe\n"
              "    [/func_tests/]\n")