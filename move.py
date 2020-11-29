import numpy as np;


def moves() -> object:
    # Define direction
    U = np.array([0, 1])
    D = np.array([0, -1])
    L = np.array([-1, 0])
    R = np.array([1, 0])

    # Define moving instruction
    moves_lst = input("Enter the instruction:")

    # Define original position
    x, y = input("Enter original position:").split()
    x = int(x)
    y = int(y)
    original_position = [x, y]
    print("Original position:", original_position)

    # Ready to move
    print("Planned moving steps:", moves_lst)
    new_position = original_position

    # Calculate the new position
    for i in range(0, len(moves_lst)):
        if moves_lst[i] == 'U':
            new_position = new_position + U

        elif moves_lst[i] == 'D':
            new_position = new_position + D

        elif moves_lst[i] == 'L':
            new_position = new_position + L

        elif moves_lst[i] == 'R':
            new_position = new_position + R
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
