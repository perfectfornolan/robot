import numpy as np;
import sys

def moves():
    # Define direction
    direction_u = np.array([0, 1])
    direction_d = np.array([0, -1])
    direction_l = np.array([-1, 0])
    direction_r = np.array([1, 0])
    max_retry = 6
    # Define original position
    for i in range(0,max_retry):
        try:
            original_x, original_y = input("Enter numeric original position:").replace(',', ' ').split()
            original_x = int(original_x)
            original_y = int(original_y)
            original_position = [original_x, original_y]
            print("Original position:", original_position)
            break
        except ValueError:
            print("Error times:", i, "Please input two integer.","Retry times left:", max_retry-i-1)
        if i == 5:
            print("Error times:", i+1, "This program will be stopped here")
            sys.exit(1)

    # Define moving instruction
    print("Please enter the instruction. e.g. UDLR")
    moves_lst = input("Enter the instruction:")

    # Ready to move
    print("Planned moving steps:", moves_lst)
    new_position = original_position

    # Calculate the new position
    for i in range(0, len(moves_lst)):
        if moves_lst[i] == 'U':
            new_position = new_position + direction_u

        elif moves_lst[i] == 'D':
            new_position = new_position + direction_d

        elif moves_lst[i] == 'L':
            new_position = new_position + direction_l

        elif moves_lst[i] == 'R':
            new_position = new_position + direction_r
        if i < (len(moves_lst) - 1):
            print("Step", i + 1, "New position:", new_position)

    # Compare final position to the original position
    print("Final position", new_position)
    comparison = new_position == original_position
    equal_arrays = comparison.all()
    if equal_arrays:
        print("Back to original position")
    else:
        print("Move away from the original position")


if __name__ == '__main__':
    moves()
