import numpy as np;


def dict():
    # Define direction
    dict_direction = {"U": np.array([0, 1]),
                      "D": np.array([0, -1]),
                      "L": np.array([-1, 0]),
                      "R": np.array([1, 0])
                      }
    return dict_direction


def max_retry():
    times = 5
    return times
