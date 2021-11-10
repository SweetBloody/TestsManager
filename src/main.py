'''
v.2.0
1. Запрашиваем количество позитивов и негативов

2. В цикле для каждого теста
- введите аргументы командной строки -> их кидаем в файл args
- введите значения для записи во входной файл (окончание ввода -> ^) -> их кидаем в файл in
- запуск программы с введенными параметрами и данными -> их кидаем в файл out

+ Добавить меню
1. Ввести путь для сохранения тестов
2. Ввести путь исполнительного файла (.exe)
3. Ввести позитивные тесты
4. Ввести негативные тесты
5. Изменить отдельный тест
0. Выход
'''
from test_process import *


def main():
    choice = -1
    if if_exists("", "func_tests"):
        tests_path = "func_tests\\"
    else:
        tests_path = ""
    exe_path = ""
    while choice != 0:
        choice = menu()
        if choice == 1:
            tests_path = input_path("Введите путь папки для сохранения тестов:\n")
        elif choice == 2:
            exe_path = input_path("Введите путь нахождения исполнительного файла:\n")
        elif choice == 3:
            if tests_path == "":
                tests_path = create_test_dir()
            if if_exists(exe_path, "app.exe"):
                pos_amount = input_tests_amount("pos")
                make_tests(pos_amount, "pos", tests_path, exe_path)
        elif choice == 4:
            if tests_path == "":
                tests_path = create_test_dir()
            if if_exists(exe_path, "app.exe"):
                neg_amount = input_tests_amount("neg")
                make_tests(neg_amount, "neg", tests_path, exe_path)
        elif choice == 5:
            if tests_path == "":
                tests_path = create_test_dir()
            if if_exists(exe_path, "app.exe"):
                mode = input_test_type()
                index = input_number("Введите номер теста, который хотите изменить:\n")
                make_test(index, mode, tests_path, exe_path)
        elif choice == -1:
            info()


if __name__ == "__main__":
    main()