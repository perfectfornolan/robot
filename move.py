import sys
import modu


class Robot:
    def moves():
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
                    position_list.append(new_position)
                    print("Original position:", original_position)
                    break
                except ValueError:
                    if i == max_retry - 1:
                        modu.err("This program will be stopped here.", i, max_retry)
                        sys.exit(1)
                    else:
                        modu.err("Please enter TWO numbers", i, max_retry)

            return new_position, original_position, position_list

        # Define moving sequence
        def new_list():
            for i in range(0, max_retry):
                moves_lst = input("Please enter the instruction. e.g. UDLR ").upper()
                if i == max_retry - 1:
                    modu.err("This program will be stopped here.", i, max_retry)
                    sys.exit(1)
                elif any(x not in dict_direction.keys() for x in moves_lst):
                    modu.err("Directional characters only", i, max_retry)
                else:
                    print("Planned moving steps:", moves_lst)
                    break
            return moves_lst

        # Define the overall new moving position
        def moving_route(moves_lst, dict_direction, new_position):
            for i in range(0, len(moves_lst)):
                if moves_lst[i] in dict_direction.keys():
                    new_position = new_position + dict_direction[moves_lst[i]]
                    position_list.append(new_position)
                if i < (len(moves_lst) - 1):
                    print("Step", i + 1, "New position:", new_position)
                else:
                    print("Final position: ", new_position)
            return new_position

        new_position, original_position, position_list = new_start()
        moves_lst = new_list()
        new_position = moving_route(moves_lst, dict_direction, new_position)

        # Compare final position to the original position
        modu.compare(new_position, original_position)


if __name__ == '__main__':
    Robot.moves()
