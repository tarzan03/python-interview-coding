def create_triangle(number_of_rows):
    if not number_of_rows:
        print("Please enter a number")
    else:
        space = 0
        for num in range(number_of_rows, 0, -1):
            print(" "*space, end="")
            print("*"*num)
            space += 1

create_triangle(5)