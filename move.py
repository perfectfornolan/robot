import sys
import modu
import location
import pandas as pd
import stringinput
import matplotlib.pyplot as plt


class Robot:

    def moves():
        # Define direction
        dict_direction = modu.dict_info()
        max_retry = modu.max_retry()
        position_list = []
        new_position, original_position, position_list = location.new_start()
        step_list = []
        # Define moving sequence

        def new_list():
            for i in range(0, max_retry):
                moves_lst = stringinput.wholestring()

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
        def moving_route(new_position, moves_lst):
            for i in range(0, len(moves_lst)):
                if moves_lst[i] in dict_direction.keys():
                    new_position = new_position + dict_direction[moves_lst[i]]
                    position_list.append(new_position)
                    step_list.append(moves_lst[i])
            return new_position, position_list, step_list

        moves_lst = new_list()
        final_position, position_list,step_list = moving_route(new_position, moves_lst)

        # output to csv file
        route = pd.DataFrame(data=position_list, columns=["Axis: X", "Axis: Y"])
        step_list.insert(0, "-")
        route['Step'] = step_list
        print(route)
        route.to_csv('route.csv')

        # Compare final position to the original position
        modu.compare(final_position, original_position)

        # output graph
        x_position_list = route["Axis: X"].values.tolist()
        y_position_list = route["Axis: Y"].values.tolist()
        length = len(x_position_list)-1
        for i in range(0,length):
            plt.arrow(x_position_list[i], y_position_list[i], x_position_list[i+1]- x_position_list[i],y_position_list[i+1]- y_position_list[i], width=0.02, color="r")
        plt.title("Testing")
        plt.show()


if __name__ == '__main__':
    Robot.moves()
