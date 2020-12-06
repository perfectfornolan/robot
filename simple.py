original_x: object
original_x, original_y = input("Enter numeric original position: ").replace(',', ' ').split()
        original_x = int(original_x)
        original_y = int(original_y)
        original_position = [original_x, original_y]
        print("Original position:", original_position)
        new_position = original_position