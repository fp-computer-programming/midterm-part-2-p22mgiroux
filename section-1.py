# Author: MOG 12/15/21

import random

def name_clones():
    names = []
    active = 1
    while active != 0:
        y_or_n = input("Name a clone? ")
        if y_or_n.lower() == "y":
            number = random.choice(range(10000))
            if len(str(number)) == 1:
                print(number)
                number = "CT-000{}".format(number)
                print(number)
                names.append(number)
            elif len(str(number)) == 2:
                number = "CT-00{}".format(number)
                names.append(number)
            elif len(str(number)) == 3:
                number = "CT-0{}".format(number)
                names.append(number)
            elif len(str(number)) == 4:
                print(number)
                number = "CT-{}".format(number)
                print(number)
                names.append(number)
            else:
                print("Try again.")
            print("New clone trooper name: {}".format(number))
        else:
            print(names)
            active = 0

name_clones()
