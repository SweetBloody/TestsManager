'''
TestsManager
v.2.0.0
'''


from run_mode import *
from cdio import info


def main():
    info(0)
    choice = mode_choose()
    if choice == 1:
        file_mode()
    else:
        manual_mode()


if __name__ == "__main__":
    main()
