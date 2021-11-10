import os
from cdio import *


# Составление названия текстового файла
def get_file_name(tests_path, mode, index, type):
    if index < 10:
        file_name = str(tests_path) + str(mode) + "_0" + str(index) + "_" + str(type) + ".txt"
    else:
        file_name = str(tests_path) + str(mode) + "_" + str(index) + "_" + str(type) + ".txt"
    return file_name


# Запуск исполнительного файла с записью результата в файл
def run_programm(exe_path, args, in_file, out_file):
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


# Создание теста
def make_test(index, mode, tests_path, exe_path):
    print("ТЕСТ {0}\n".format(index))
    args_file = get_file_name(tests_path, mode, index, "args")
    in_file = get_file_name(tests_path, mode, index, "in")
    out_file = get_file_name(tests_path, mode, index, "out")
    args = input_arguments()
    print_args_to_file(args_file, args)
    text = input_data("Введите данные для входного файла (для окончания ввода - символ '^')")
    print_data_to_file(in_file, text)
    run_programm(exe_path, args, in_file, out_file)


# Создание тестов
def make_tests(amount, mode, tests_path, exe_path):
    if mode == "pos":
        print("\n\nПОЗИТИВНЫЕ ТЕСТЫ:\n")
    else:
        print("\n\nНЕГАТИВНЫЕ ТЕСТЫ:\n")

    for i in range(1, amount + 1):
        make_test(i, mode, tests_path, exe_path)
