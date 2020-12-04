import sys
import modu
import location
import pandas as pd
import plotly.express as px

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
        def moving_route(new_position, moves_lst):
            for i in range(0, len(moves_lst)):
                if moves_lst[i] in dict_direction.keys():
                    new_position = new_position + dict_direction[moves_lst[i]]
                    position_list.append(new_position)
                    step_list.append(moves_lst[i])
            return new_position, position_list, step_list

        moves_lst = new_list()
        final_position, position_list,step_list = moving_route(new_position, moves_lst)

        data_range = position_list
        route = pd.DataFrame(data=data_range, columns=["Axis: X", "Axis: Y"])
        step_list.insert(0, "-")
        route['Step'] = step_list
        print(route)
        route.to_csv('route.csv')

        # Compare final position to the original position
        modu.compare(final_position, original_position)

        # fig = px.line(route, x='Axis: X', y='Axis: Y', title='Point')
        # fig.show()


if __name__ == '__main__':
    Robot.moves()
