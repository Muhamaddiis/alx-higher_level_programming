#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    my_list[1, 2, 3]
    total = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
        except IndexError:
            break
        else:
            total += 1
    print()
    return (total)