import numpy as np
import math


# Define direction
def dict_info():
    dict_direction = {"U": np.array([0, 1]),
                      "D": np.array([0, -1]),
                      "L": np.array([-1, 0]),
                      "R": np.array([1, 0])
                      }
    return dict_direction


# Define max retry times
def max_retry():
    times = 5
    return times


# Function: Compare value
def compare(final_position, original_position):
    comparison = final_position == original_position
    equal_arrays = comparison.all()
    distance(final_position, original_position)
    if equal_arrays:
        return print("Back to original position")
    else:
        return print("Move away from the original position")


# Function: Calculate distance between twp points
def distance(new_position, original_position):
    length = math.dist(new_position, original_position)
    print("Distance between the start and end point: ", length)


# Function: error message
def err(msg, i, max_retry):
    print("Error times:", i + 1)
    print(msg)
    print("Retry times left:", max_retry - i - 1)
    print("\n")

