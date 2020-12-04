import sys
import modu
import pandas as pd
import numpy as np

# Define direction
dict_direction = modu.dict_info()
max_retry = modu.max_retry()
position_list = []


# Define original position

def new_start():
    for i in range(0, max_retry):
        try:
            original_x, original_y = input("Enter numeric original position: ").replace(',', ' ').split()
            new_position = original_position = [int(original_x), int(original_y)]
            position_list.append(original_position)
            print("Original position:", original_position)
            break
        except ValueError:
            if i == max_retry - 1:
                modu.err("This program will be stopped here.", i, max_retry)
                sys.exit(1)
            else:
                modu.err("Please enter TWO numbers", i, max_retry)

    return new_position, original_position, position_list


if __name__ == '__main__':
    new_start()
