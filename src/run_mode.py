import cdio as c
import test_process as t
import example_file as e


def manual_mode():
    choice = -1
    if t.if_exists("", "func_tests"):
        tests_path = "func_tests\\"
    else:
        tests_path = ""
    exe_path = ""
    out_file_mode = c.is_out_file()
    while choice != 0:
        choice = c.manual_menu()
        if choice == 1:
            tests_path = c.input_path("Введите путь папки для сохранения тестов:\n")
        elif choice == 2:
            exe_path = c.input_path("Введите путь нахождения исполнительного файла:\n")
        elif choice == 3:
            if tests_path == "":
                tests_path = t.create_test_dir()
            if t.if_exists(exe_path, "app.exe"):
                pos_amount = c.input_tests_amount("pos")
                t.make_tests(pos_amount, "pos", tests_path, exe_path, out_file_mode, 2)
        elif choice == 4:
            if tests_path == "":
                tests_path = t.create_test_dir()
            if t.if_exists(exe_path, "app.exe"):
                neg_amount = c.input_tests_amount("neg")
                t.make_tests(neg_amount, "neg", tests_path, exe_path, out_file_mode, 2)
        elif choice == 5:
            if tests_path == "":
                tests_path = t.create_test_dir()
            if t.if_exists(exe_path, "app.exe"):
                mode = c.input_test_type()
                index = c.input_number("Введите номер теста, который хотите изменить:\n")
                t.manual_make_test(index, mode, tests_path, exe_path, out_file_mode)
        elif choice == -1:
            c.info(2)


def file_mode():
    choice = -1
    if t.if_exists("", "func_tests"):
        tests_path = "func_tests\\"
    else:
        tests_path = ""
    exe_path = ""
    out_file_mode = c.is_out_file()
    while choice != 0:
        choice = c.file_menu()
        if choice == 1:
            tests_path = c.input_path("Введите путь папки для сохранения тестов:\n")
        elif choice == 2:
            exe_path = c.input_path("Введите путь нахождения исполнительного файла:\n")
        elif choice == 3:
            if tests_path == "":
                tests_path = t.create_test_dir()
            if t.if_exists(exe_path, "app.exe"):
                pos_amount = c.input_tests_amount("pos")
                t.make_tests(pos_amount, "pos", tests_path, exe_path, out_file_mode, 1)
        elif choice == 4:
            if tests_path == "":
                tests_path = t.create_test_dir()
            if t.if_exists(exe_path, "app.exe"):
                neg_amount = c.input_tests_amount("neg")
                t.make_tests(neg_amount, "neg", tests_path, exe_path, out_file_mode, 1)
        elif choice == -1:
            c.info(1)
        elif choice == -2:
            e.example_tests_file()
            e.example_tests_args_file()


def mode_choose():
    print("Выберите режим работы программы (вариант ввода тестов):\n"
          " 1. Ввод данных для тестов с помощью файла настроек (файл с данными для тестов)\n"
          " 2. Ввод данных для тестов вручную в консоль в TestsManager\n")
    choice = c.input_number("Введите число (1/2):\n")
    return choice
