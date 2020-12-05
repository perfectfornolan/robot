
import re
import pandas as pd
import sys
import modu
def wholestring():
    max_retry = modu.max_retry()
    for i in range(0, max_retry):
        try:
            input_string = []
            input_number = []
            command_string = input("Please input required route")
            for x in command_string:
                if x.isalpha():
                    input_string += x
            input_string = list(str.upper("".join(input_string)))

            get_number = re.findall(r'\d+', command_string)
            input_number = list(map(int, get_number))
            # da = {"Step:": input_string, "Number:": input_number}
            # df = pd.DataFrame(data=da)
            # print(df)
            break
        except ValueError or IndexError:
            print("Please input with correct structure", "Retry Time Left:",i)
            # if i == max_retry - 1:
            #     modu.err("This program will be stopped here.", i, max_retry)
            #     sys.exit(1)
            # else:
            #     modu.err("Please enter TWO numbers", i, max_retry)

    wholestring = []
    length = len(input_number)
    for i in range(0, length):
        wholestring.append(input_string[i] * int(input_number[i]))

    wholestring = ''.join(map(str, wholestring))[:10]
    print(wholestring)
    return wholestring


if __name__ == '__main__':
    wholestring()