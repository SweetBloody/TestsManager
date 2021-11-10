# Ввод пути в файловой системе
def input_path(message):
    path = input(message)
    if path[len(path) - 1] != "\\":
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


# Запись аргументов в файл
def print_args_to_file(file_name, args):
    file = open(file_name, 'w')
    file.write(args + '\n')


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


# Запись данных в файл
def print_data_to_file(file_name, text):
    file = open(file_name, 'w')
    for string in text:
        file.write(string + '\n')
    file.close()


# Печать таблицы меню
def print_menu_table():
    print("┌", "─" * 50, "┐")
    print("│", "  MENU", " " * 43, "│")
    print("│", "  1. Ввести путь для сохренения тестов            ", "│")
    print("│", "  2. Ввести путь нахождения исполнительного файла ", "│")
    print("│", "  3. Ввести позитивные тесты                      ", "│")
    print("│", "  4. Ввести негативные тесты                      ", "│")
    print("│", "  5. Изменить/создать отдельный тест              ", "│")
    print("│", " -1. Важная информация о программе                ", "│")
    print("│", "  0. Выход                                        ", "│")
    print("└", "─" * 50, "┘")


# Обработка меню
def menu():
    choice = ""
    print_menu_table()
    while type(choice) == str or choice < -1 or choice > 5:
        choice = input_number("Введите необходимый пункт меню (от -1 до 5):\n")
    return choice


# Вывод информации о программе
def info():
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
          "   называться app.exe;\n"
          " - чтобы завершить ввод данных для входного файла нужно последней\n"
          "   строкой ввести символ '^'\n\n"
          "Пример директории для корректной работы программы (если вы не\n"
          "указываете пути для исполняемого файла вашей программы и папки\n"
          "для сохранения тестов):\n"
          "/some_dir/\n"
          "    TestsManager.exe\n"
          "    app.exe\n"
          "    [/func_tests/]\n")
