#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for i in range(x):
            print(my_list[i], end=' ')
            counter += 1
        print()
        return counter
    except IndexError:
        for i in range(x):
            try:
                print(my_list[i], end=' ')
            except IndexError:
                break
            counter += 1
        print()
        return counter
