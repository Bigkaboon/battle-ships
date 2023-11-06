import random

user_name = ""
grid_size = 7
user_grid = []
pc_grid = []
random_coordinates = ""
letter_list = "ABCDEFGHIJKL"
p_guess = ""
pc_guess = ""
boats_left = 0
p_right_guess = []
pc_right_guess = []
p_wrong_guess = []
pc_wrong_guess = []


def clear_console():
    """ clearing console once needed """
    print("\n" * 50)


def validate_input(current_input, valid_options):
    return current_input in valid_options


def get_user_name():
    user_name = input("Enter a username \n")
    while len(user_name) < 3:
        user_name = input("""Usernames should be at least 3 chars long,
        please enter a username! \n""")
    return user_name


def get_grid_size():
    grid_size = input("""What grid size would you like to play on \n
    1. EASY : 7x7 \n
    2. MEDIUM : 9x9 \n
    3. HARD : 12x12 \nAnswer with a number 1-3 \n""")
    while validate_input(grid_size, ["1", "2", "3"]) is False:
        grid_size = input("""Invalid input, What grid size would
        you like to play on \n
        1. EASY : 7x7 \n
        2. MEDIUM : 9x9 \n
        3. HARD : 12x12 \nAnswer with a number 1-3 \n""")
    if grid_size == "1":
        grid_size = 7
    if grid_size == "2":
        grid_size = 9
    if grid_size == "3":
        grid_size = 12
    return grid_size


def get_user_ships_mode():
    want_random = 0
    while want_random not in ["1", "2"]:
        want_random = input("""How do you want you ships to be placed \n
        1. Randomly \n
        2. Manually\nAnswer 1 or 2.""")
        if validate_input(want_random, ["1", "2"]) is False:
            print("Must enter either 1 or 2, please try again.")
    return want_random


def create_empty_grid(grid_size):
    index = 0
    grid = []
    while index < grid_size:
        grid.append(["_" for i in range(0, grid_size)])
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
        if (grid[x_coordinate][y_coordinate] == "_"):
            grid[x_coordinate][y_coordinate] = "X"
            ships_placed += 1
    return grid


def translate_coordinates(coordinate, grid_size):
    letter = coordinate[0]
    valid_letters = letter_list[0: grid_size]
    if validate_input(letter.upper(), valid_letters) is False:
        print(f"Please enter one of these letter {valid_letters}")
        return False
    else:
        input_number = coordinate[1:]
        try:
            int_input_number = int(input_number)
            if int_input_number <= grid_size and int_input_number >= 1:
                return (valid_letters.index(letter.upper()),
                        int_input_number - 1)
            else:
                print(f"Please enter a number >=1 and <={grid_size}")
                return False
        except ValueError:
            print(f"Please enter a number for the second coordinate")
            False
    if coordinate[1:] is not int:
        return False
    if letter == "" or " ":
        return False


def place_ships_manually(grid, grid_size):
    ships_placed = 0
    while ships_placed < grid_size:
        valid_coordinate = False
        while valid_coordinate is False:
            coordinate = input("Enter a coordinate (A6):")
            while len(coordinate) <= 1:
                coordinate = input("""Input can't be empty!
                Please enter a coordinate (A6):""")
            translated_coordinate = translate_coordinates(
                                        coordinate, grid_size)
            tr_coord = translated_coordinate
            if translated_coordinate is not False:
                if (grid[translated_coordinate[0]]
                        [translated_coordinate[1]]
                        == "_"):
                    grid[tr_coord[0]][tr_coord[1]] = "X"
                    ships_placed += 1
                    valid_coordinate = True
                else:
                    print(f"""The current coordinate already has a ship,
                    please enter a different one""")
    return grid


def place_user_ships(user_grid, grid_size):
    """ Lets the user place X's representing the ships """
    ship_mode = get_user_ships_mode()
    if ship_mode == "1":
        user_grid = place_random_ships(user_grid, grid_size)
    if ship_mode == "2":
        place_ships_manually(user_grid, grid_size)
    return user_grid


def player_guess(grid_size):
    translated_p_guess = False
    while translated_p_guess is False:
        p_guess = input("Guess a coordinate (A6): ")
        while len(p_guess) <= 1 or "":
            p_guess = input("""Input can't be empty!
                Please guess a coordinate (A6): """)
        translated_p_guess = translate_coordinates(p_guess, grid_size)
        if translated_p_guess is not False:
            print(f"Your guess is {p_guess}")
            translated_p_guess = True
        else:
            print("Your guess is not valid")
    return p_guess


def print_line():
    print("-------------------------\n")


def computer_guess(grid_size):
    x_coordinate = random.randint(0, grid_size - 1)
    y_coordinate = random.randint(1, grid_size - 1)
    x_letter_coordinate = letter_list[x_coordinate]

    pc_guess = x_letter_coordinate + str(y_coordinate)
    print(f"Computer guessed {pc_guess}")
    return pc_guess


def handle_computer_guess(grid, grid_size):
    guess = computer_guess(grid_size)
    while guess in pc_wrong_guess:
        guess = computer_guess(grid_size)
    translated_guess = translate_coordinates(guess, grid_size)
    if translated_guess is not False:
        if (grid[translated_guess[0]][translated_guess[1]] == "X"):
            grid[translated_guess[0]][translated_guess[1]] = 1
            print("Computer guessed right")
            pc_right_guess.append(guess)
        else:
            grid[translated_guess[0]][translated_guess[1]] = 0
            pc_wrong_guess.append(guess)
            return pc_wrong_guess


def show_guesses(wrong_guess, right_guess):
    print(f"This is the wrong guesses:\n{wrong_guess}\n")
    print(f"This is the right guesses:\n{right_guess}\n")


def handle_player_guess(grid, grid_size):
    guess = player_guess(grid_size)
    while guess in p_wrong_guess:
        print("You have already guessed that coordinate")
        guess = player_guess(grid_size)
    translated_guess = translate_coordinates(guess, grid_size)
    if translated_guess is not False:
        if (grid[translated_guess[0]][translated_guess[1]] == "X"):
            grid[translated_guess[0]][translated_guess[1]] = 1
            p_right_guess.append(guess)
            print("You guessed right")
            print(f"Right guesses: {p_right_guess}")
        else:
            grid[translated_guess[0]][translated_guess[1]] = 0
            print("Wrong guess")
            p_wrong_guess.append(guess)
            print(f"Wrong guesses: {p_wrong_guess}")
            return p_wrong_guess


def show_stats(user_name, grid_size):
    print(f"{user_name}'s right guesses: {len(p_right_guess)}")
    print(f"Computer's right guesses: {len(pc_right_guess)}")
    print(f"First to {grid_size}")


def determine_winner(
        winner, p_right_guess, pc_right_guess, grid_size, user_name):
    if len(p_right_guess) == grid_size:
        print(f"Congrats {user_name}! You Win!.")
        return True
    elif len(pc_right_guess) == grid_size:
        print("GAME OVER! The computer wins.")
        return True
    else:
        winner = False


def start_game():
    user_name = get_user_name()
    clear_console()
    print(f"Hello {user_name}\n")
    grid_size = get_grid_size()
    clear_console()
    user_grid = create_empty_grid(grid_size)
    pc_grid = create_empty_grid(grid_size)
    pc_grid = place_random_ships(pc_grid, grid_size)
    clear_console()
    user_grid = place_user_ships(user_grid, grid_size)
    clear_console()
    winner = False
    while winner is not True:
        clear_console()
        print_line()
        print(f"Computer's guesses:\n")
        show_guesses(pc_wrong_guess, pc_right_guess)
        print_line()
        print(f"{user_name}'s guesses:\n")
        show_guesses(p_wrong_guess, p_right_guess)
        print_line()
        print_grid(user_grid, grid_size)
        show_stats(user_name, grid_size)
        handle_player_guess(pc_grid, grid_size)
        determine_winner(
            winner, p_right_guess, pc_right_guess, grid_size, user_name)
        handle_computer_guess(user_grid, grid_size)
        print_grid(user_grid, grid_size)
        winner = determine_winner(
            winner, p_right_guess, pc_right_guess, grid_size, user_name)
        if winner is True:
            print("Game has ended")
            break


if __name__ == "__main__":
    start_game()
