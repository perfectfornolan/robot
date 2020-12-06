import re
import modu


def wholestring():
    max_retry = modu.max_retry()
    for i in range(0, max_retry):
        input_content = input("Please input required route")
        all_string = []
        if len(input_content) == 0:
            print("Please Input!", "Your can retry ", max_retry-i, "Times only")
            continue

        for x in input_content:
            if x.isalpha():
                all_string += x

        all_string = list(str.upper("".join(all_string)))
        all_number = list(map(int, re.findall(r'\d+', input_content)))
        wordstring = ""

        if len(all_number) == len(all_string) >0:
            for i in range(0, len(all_string)):
                wordstring = wordstring + all_string[i] * int(all_number[i])
                print("Great input")
            return wordstring

        elif len(all_number) == 0:
            wordstring = input_content
            print("Great input")
            return wordstring

        else:
            print("Please input with correct format")
            print("Please Input!", "Your can retry ", max_retry-i, "Times only")
            continue
    print("GG")


if __name__ == '__main__':
    wholestring()
