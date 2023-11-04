import random

user_name = ""
grid_size = 7
user_grid = []
pc_grid = []


def clear_console():
    """ clearing console once needed """
    print("\n" * 50)


def validate_input(current_input, valid_options):
    return current_input in valid_options


def get_user_name():
    user_name = input("Enter a username \n")
    while len(user_name) < 3:
        return user_name


def get_grid_size():
    grid_size = input("What grid size would you like to play on \n1. EASY : 7x7 \n2. MEDIUM : 9x9 \n3. HARD : 12x12 \nAnswer with a number 1-3 \n")
    while validate_input(grid_size, ["1", "2", "3"]) is False:
        grid_size = input("Invalid input, What grid size would you like to play on \n1. EASY : 7x7 \n2. MEDIUM : 9x9 \n3. HARD : 12x12 \nAnswer with a number 1-3 \n")  

    if grid_size == "1":
        grid_size = 7
    if grid_size == "2":
        grid_size = 9
    if grid_size == "3":
        grid_size == 12
    return grid_size


def create_empty_grid(grid_size):
    index = 0
    grid = []
    while index < grid_size:
        grid.append([0 for i in range(0, grid_size)])
        index = index + 1
    return grid


def print_grid(grid, grid_size):
    index = 1
    number_list = "   "
    border = "***"
    while index <= grid_size:
        number_list += f"{index}"
        index = index + 1
        border += "***"
    letter_list = "ABCDEFGHIJKL"
    index = 0
    print(f"{border}\n")
    print(f"{number_list}\n")
    for row in grid:
        row_list = f"{letter_list[index]}  "
        for item in row:
           row_list += f"{item}  "
        print(f"{row_list}\n")
        index = index + 1
    print(border)


def start_game():
    user_name = get_user_name()
    print(f"Hello {user_name}\n")
    grid_size = get_grid_size()
    user_grid = create_empty_grid(grid_size)
    pc_grid = create_empty_grid(grid_size)
    print_grid(user_grid, grid_size)


