import random

user_name = ""
grid_size = 7
user_grid = []
pc_grid = []
random_coordinates = ""
letter_list = "ABCDEFGHIJKL"
p_guess = ""
pc_guess = ""



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
        want_random = input("How do you want you ships to be placed \n1. Randomly \n2. Manually\nAnswer 1 or 2.")
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
        x_coordinate = random.randint(0, grid_size - 1)
        y_coordinate = random.randint(0, grid_size - 1)
        if (grid[x_coordinate][y_coordinate] == 0):
            grid[x_coordinate][y_coordinate] = "X"
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
            else:
                print(f"Please enter a number >=1 and <={grid_size}")
                return False
        except ValueError:
            print(f"Please enter a number for the second coordinate")
            False


def place_ships_manually(grid, grid_size):
    ships_placed = 0
    while ships_placed < grid_size:
        valid_coordinate = False
        while valid_coordinate is False:
            coordinate = input("Enter a coordinate (A6):")
            translated_coordinate = translate_coordinates(coordinate, grid_size)
            if translated_coordinate is not False:
                if (grid[translated_coordinate[0]][translated_coordinate[1]] == 0):
                    grid[translated_coordinate[0]][translated_coordinate[1]] = "X"
                    ships_placed += 1
                    valid_coordinate = True
            else:
                print(f"The current coordinate already has a ship, please enter a different one")
    return grid


def place_user_ships(user_grid, grid_size):
    """ Lets the user place X's representing the ships """
    ship_mode = get_user_ships_mode()
    if ship_mode == "1":
        user_grid = place_random_ships(user_grid, grid_size)
    if ship_mode == "2":
        place_ships_manually(user_grid, grid_size)
    return user_grid


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


def player_guess():
    translated_p_guess = False
    while translated_p_guess is False:
        p_guess = input("Guess a coordinate (A6): ")
        translated_p_guess = translate_coordinates(p_guess, grid_size)
        if translated_p_guess is not False:
            print("Your guess is valid")
            print(f"Your guess is {p_guess}")
            translated_p_guess = True
        else:
            print("Your guess is not valid")
    return p_guess
    


def computer_guess():
    x_coordinate = random.randint(0, grid_size - 1)
    y_coordinate = random.randint(0, grid_size - 1)
    x_letter_coordinate = letter_list[x_coordinate]

    pc_guess = x_letter_coordinate + str(y_coordinate)
    print(pc_guess)
    return pc_guess
    

def handle_computer_guess(grid):
    guess = computer_guess()
    translated_guess = translate_coordinates(guess, grid_size)
    if translated_guess is not False:
        if (grid[translated_guess[0]][translated_guess[1]] == "X"):
            grid[translated_guess[0]][translated_guess[1]] = 1
            print("Computer guessed right")
        else:
            grid[translated_guess[0]][translated_guess[1]] = 2
            print("Comupter guessed wrong")


def handle_player_guess(grid):
    guess = player_guess()
    translated_guess = translate_coordinates(guess, grid_size)
    if translated_guess is not False:
        if (grid[translated_guess[0]][translated_guess[1]] == "X"):
            grid[translated_guess[0]][translated_guess[1]] = 1
            print("You guessed right")
        else:
            grid[translated_guess[0]][translated_guess[1]] = 2
            print("Wrong guess")

            
def play_game():
    handle_player_guess(pc_grid)
    print_grid(pc_grid, grid_size)
    

    


def start_game():
    user_name = get_user_name()
    print(f"Hello {user_name}\n")
    grid_size = get_grid_size()
    user_grid = create_empty_grid(grid_size)
    pc_grid = create_empty_grid(grid_size)
    pc_grid = place_random_ships(pc_grid, grid_size)
    print_grid(pc_grid, grid_size)
    user_grid = place_user_ships(user_grid, grid_size)
    print_grid(user_grid, grid_size)
    handle_computer_guess(user_grid)
    print_grid(user_grid, grid_size)
    
    
    
if __name__ == "__main__":
    start_game()
