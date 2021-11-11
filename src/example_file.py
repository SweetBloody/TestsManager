# Создание примера файла настроек со вхоными данными программы
def example_tests_file():
    file = open("tests.txt", 'w')
    for i in range(3):
        for j in range(1, 6):
            file.write("String {0}\n".format(j))
        file.write("-----\n")
    file.close()


# Создание примера файла настроек с аргументами командной строки
def example_tests_args_file():
    file = open("tests_args.txt", 'w')
    for i in range(1, 4):
        file.write("Argument_{0} ".format(i))
    file.write("\n")
    for i in range(1, 2):
        file.write("Argument_{0} ".format(i))
    file.write("\n")
    for i in range(1, 3):
        file.write("Argument_{0} ".format(i))
    file.write("\n")
