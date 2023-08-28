#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if my_list is None:
        return (None)
    a = 0
    while True:
        try:
            if a < x:
                print("{}".format(my_list[a]), end='')
                a += 1
            else:
                print()
                return (a)
        except IndexError:
            print()
            return (a)
