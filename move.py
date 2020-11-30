import numpy as np;
import sys
import math

class Robot:
    def moves():
        # Define direction
        dict_direction = {"U": np.array([0, 1]),
                          "D": np.array([0, -1]),
                          "L": np.array([-1, 0]),
                          "R": np.array([1, 0])
                          }
        max_retry = 5

        # Function: show error message
        def err(msg):
            print("Error times:", i + 1)
            print(msg)
            print("Retry times left:", max_retry - i - 1)
            print("\n")

        # Function: Compare value
        def compare():
            comparison = new_position == original_position
            equal_arrays = comparison.all()
            if equal_arrays:
                print("Back to original position")
            else:
                print("Move away from the original position")
                distance()

        # Function: Calculate distance between twp points
        def distance():
            length = (math.dist(original_position, new_position))
            print("Distance: ", length)

        # Define original position
        for i in range(0, max_retry):
            try:
                original_x, original_y = input("Enter numeric original position: ").replace(',', ' ').split()
                new_position = original_position = [int(original_x), int(original_y)]
                print("Original position:", original_position)
                break
            except ValueError:
                if i == max_retry - 1:
                    err("This program will be stopped here.")
                    sys.exit(1)
                else:
                    err("Please enter TWO numbers")

        # Define moving sequence
        for i in range(0, max_retry):
            moves_lst = input("Please enter the instruction. e.g. UDLR ").upper()
            if i == max_retry - 1:
                err("This program will be stopped here.")
                sys.exit(1)
            elif any(x not in dict_direction.keys() for x in moves_lst):
                err("Directional characters only")
            else:
                print("Planned moving steps:", moves_lst)
                break

        # Calculate new position
        for i in range(0, len(moves_lst)):
            if moves_lst[i] in dict_direction.keys():
                new_position = new_position + dict_direction[moves_lst[i]]
            if i < (len(moves_lst) - 1):
                print("Step", i + 1, "New position:", new_position)
            if i == len(moves_lst) - 1:
                print("Final position: ", new_position)

        # Compare final position to the original position
        compare()


if __name__ == '__main__':
    Robot.moves()
