import os
import cdio as c


# Составление названия текстового файла
def get_file_name(tests_path, mode, index, type):
    if index < 10:
        file_name = str(tests_path) + str(mode) + "_0" + str(index) + "_" + str(type) + ".txt"
    else:
        file_name = str(tests_path) + str(mode) + "_" + str(index) + "_" + str(type) + ".txt"
    return file_name


def get_file_name_for_args(mode, index, type):
    if index < 10:
        file_name = str(mode) + "_0" + str(index) + "_" + str(type) + ".txt"
    else:
        file_name = str(mode) + "_" + str(index) + "_" + str(type) + ".txt"
    return file_name


def get_double_file_name(tests_path, mode, index, type, number):
    if index < 10:
        file_name = str(tests_path) + str(mode) + "_0" + str(index) + "_" + str(type) + "_" + str(number) + ".txt"
    else:
        file_name = str(tests_path) + str(mode) + "_" + str(index) + "_" + str(type) + "_" + str(number) + ".txt"
    return file_name


def get_double_file_name_for_args(mode, index, type, number):
    if index < 10:
        file_name = str(mode) + "_0" + str(index) + "_" + str(type) + "_" + str(number) + ".txt"
    else:
        file_name = str(mode) + "_" + str(index) + "_" + str(type) + "_" + str(number) + ".txt"
    return file_name


# Запуск исполнительного файла с записью результата в файл
def run_programm(exe_path, args, in_file, out_file, out_file_mode):
    if out_file_mode == 1:
        os.system("{0}app.exe {1} {2} {3}".format(exe_path, in_file, out_file, args))
    else:
        os.system("{0}app.exe {1} {2} > {3}".format(exe_path, in_file, args, out_file))


# Создание папки для тестов
def create_test_dir():
    os.system("mkdir func_tests")
    tests_path = "func_tests\\"
    return tests_path


# Проверка существования исполняемого файла
def if_exists(path, name):
    check = os.path.exists("{0}{1}".format(path, name))
    if check == False and name != "func_tests":
        print("В текущей папке нет {0}!\n".format(name))
    return check


# Создание теста вручную  TODO: СДЕЛАТЬ ДВОЙНОЙ ВХОДНОЙ ФАЙЛ
def manual_make_test(index, mode, tests_path, exe_path, out_file_mode, in_file_mode):
    print("ТЕСТ {0}\n".format(index))
    args_file = get_file_name(tests_path, mode, index, "args")
    in_file = get_file_name(tests_path, mode, index, "in")
    out_file = get_file_name(tests_path, mode, index, "out")
    args = c.input_arguments()
    c.print_args_to_file(args_file, args, mode, index, out_file_mode, in_file_mode)
    text = c.input_data("Введите данные для входного файла (для окончания ввода - символ '^')")
    c.print_data_to_file(in_file, text, 2)
    run_programm(exe_path, args, in_file, out_file, out_file_mode)


# Создание теста с помощью файла настроек
def file_make_test(setting_file_1, setting_file_2, args_setting_file,
                   index, mode, tests_path, exe_path, out_file_mode, in_file_mode):
    args_file = get_file_name(tests_path, mode, index, "args")
    if in_file_mode == 1:
        in_file = get_file_name(tests_path, mode, index, "in")
        out_file = get_file_name(tests_path, mode, index, "out")
        args = c.input_arguments_from_file(args_setting_file)
        c.print_args_to_file(args_file, args, mode, index, out_file_mode, in_file_mode)
        text = c.input_data_from_file(setting_file_1)
        c.print_data_to_file(in_file, text, 1)
    else:
        in_file_1 = get_double_file_name(tests_path, mode, index, "in", 1)
        in_file_2 = get_double_file_name(tests_path, mode, index, "in", 2)
        in_file = in_file_1 + " " + in_file_2
        out_file = get_file_name(tests_path, mode, index, "out")
        args = c.input_arguments_from_file(args_setting_file)
        c.print_args_to_file(args_file, args, mode, index, out_file_mode, in_file_mode)
        text_1 = c.input_data_from_file(setting_file_1)
        c.print_data_to_file(in_file_1, text_1, 1)
        text_2 = c.input_data_from_file(setting_file_2)
        c.print_data_to_file(in_file_2, text_2, 1)
    run_programm(exe_path, args, in_file, out_file, out_file_mode)


# Создание тестов
def make_tests(amount, mode, tests_path, exe_path, out_file_mode, run_mode, in_file_mode):
    if run_mode == 1:
        setting_file_2 = open("tests_2.txt", 'r')
        if in_file_mode == 1:
            setting_file_1 = open("tests.txt", 'r')
        else:
            setting_file_1 = open("tests_1.txt", 'r')
        args_setting_file = open("tests_args.txt", 'r')
        for i in range(1, amount + 1):
            file_make_test(setting_file_1, setting_file_2, args_setting_file, i, mode, tests_path, exe_path, out_file_mode, in_file_mode)
        setting_file_1.close()
        setting_file_2.close()
        args_setting_file.close()
        print("Success!\n")
    else:
        if mode == "pos":
            print("\n\nПОЗИТИВНЫЕ ТЕСТЫ:\n")
        else:
            print("\n\nНЕГАТИВНЫЕ ТЕСТЫ:\n")
        for i in range(1, amount + 1):
            manual_make_test(i, mode, tests_path, exe_path, out_file_mode, in_file_mode)