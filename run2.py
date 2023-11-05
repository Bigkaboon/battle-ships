import random

user_name = ""
grid_size = 7
user_grid = []
pc_grid = []
random_coordinates = ""
letter_list = "ABCDEFGHIJKL"


def clear_console():
    """ clearing console once needed """
    print("\n" * 50)


def validate_input(current_input, valid_options):
    return current_input in valid_options


def get_user_name():
    user_name = input("Enter a username \n")
    while len(user_name) < 3:
        user_name = input("Usernames should be at least 3 chars long, please enter a username! \n")
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
        grid_size = 12
    return grid_size


def get_user_ships_mode():
    want_random = 0
    while want_random  not in ["1", "2"]:
        want_random = inmput("How do you want you ships to be placed \n1. Randomly \n2. Manually\nAnswer 1 or 2.")
        if validate_input(want_random, ["1", "2"]) is False:
            print("Must enter either 1 or 2, please try again.")
    return want_random


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
        number_list += f"{index}  "
        index = index + 1
        border += "***"
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

    
def place_random_ships(grid, grid_size):
    ships_placed = 0
    while ships_placed < grid_size:

        x_coordniate = random.randint(0, grid_size)
        y_coordniate = random.randint(0, grid_size)
        if (grid[x_coordniate][y_coordniate] == 0)
            grid[x_coordniate][y_coordniate] == "X"
            ships_placed += 1
    return grid


def translate_coordinates(coordinate, grid_size):
    letter = coordinate[0]
    valid_letters = letter_list[0: grid_size - 1]
    if validate_input(letter.upper(), valid_letters) is False:
        print(f"Please enter one of these letter {valid_letters}")
        return False
    else:
        input_number = coordinate[1:]
        try:
            int_input_number = int(input_number)
            if int_input_number <= grid_size and int_input_number >= 1:
                return (valid_letters.index(letter.upper()), int_input_number - 1)
        except ValueError:
            print(f"Please enter a number for the second coordinate")
            False


def place_user_ships(user_grid, grid_size):
    """ Lets the user place X's representing the ships """
    x = True
    while x is True:
        try:
            want_random = int(input("How do you want you ships to be placed \n1. Randomly \n2. Manually\nAnswe 1 or 2."))
            if want_random not in [1, 2]:
                raise ValueError("Must enter either 1 or 2, please try again.")
            
        except ValueError as ve:
            print(ve)
        
        if want_random == 2:
            for i in range(10):
                
    
                boat_coordinates = input("Write coordinates for where you want to place an 'X'")
                

                x_row, x_col = ord(boat_coordinates[0]) - ord("A"), int(boat_coordinates[1]) - 1
                

                if 0 <= x_row < len(user_grid) and 0 <= x_col < len(user_grid[0]):
                    user_grid[x_row][x_col] = "X"
                else:
                    print("Invalid coordinates for placing 'X'")
                print_grid(user_grid, grid_size)
            x = False
        elif want_random == 1:
            random_player_ships(user_grid, grid_size)
            x = False


def random_player_ships(user_grid, grid_size):
    letters = ["A", "B", "C", "D", "E", "F", "G"]
    x = 7
    if grid_size == 9:
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        x = 9
    elif grid_size == 12:
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
        x = 12

    for i in range(10):
        x_coordniate = random.choice(letters)
        y_coordniate = random.randint(1, x)
        random_boat_coordinates = x_coordniate + str(y_coordniate)
            
            
        x_row, x_col = ord(random_boat_coordinates[0]) - ord("A"), int(random_boat_coordinates[1]) - 1

        if 0 <= x_row < len(user_grid) and 0 <= x_col < len(user_grid[0]):
            user_grid[x_row][x_col] = "X"
        else:
            print("Invalid coordinates for placing 'X'")

    print_grid(user_grid, grid_size)

def start_game():
    user_name = get_user_name()
    print(f"Hello {user_name}\n")
    grid_size = get_grid_size()
    user_grid = create_empty_grid(grid_size)
    pc_grid = create_empty_grid(grid_size)
    print_grid(user_grid, grid_size)
    
    place_computer_ships(pc_grid, grid_size)
    place_user_ships(user_grid,grid_size)
    

    
if __name__ == "__main__":
    start_game()
