import random

def clear_console():
    """ clearing console once needed """
    print("\n" * 50)


def start_game():
    """ Function for setting up the game """
    user_name = input("Select a username! \n")
    print(f"Hello {user_name}\n")
    player_grid = grids()
    computer_grid = grids()
    
    clear_console()
    random_boats(computer_grid)
    place_ships(player_grid)
    
    
   
    

def grids():
    """ User choose map size """
    grid_1 = []

    for x in "ABCDEFG":
        row = [x] + [" "] * 7
        grid_1.append(row)
    
    grid_2 = []

    for x in "ABCDEFGHI":
        row = [x] + [" "] * 9
        grid_2.append(row)

    grid_3 = []

    for x in "ABCDEFGHIJKL":
        row = [x] + [" "] * 12
        grid_3.append(row)

    while True:
        try:
            grid_type_num = int(input("What grid size would you like to play on \n1. EASY : 7x7 \n2. MEDIUM : 9x9 \n3. HARD : 12x12 \nAnswer with a number 1-3 \n"))
            if grid_type_num not in [1, 2, 3]:
                raise ValueError("You have to write either 1, 2 or 3, please try again.")

        
        
            if grid_type_num == 1:
                return grid_1
            elif grid_type_num == 2:
                return grid_2
            elif grid_type_num == 3:
                return grid_3
        except ValueError as ve:
            print(ve)


def place_ships(player_grid):
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

                for row in player_grid:
                    print(row)
                #while True:
                    #try:
                        #x_coordinates = input("Write coordinates for where you want to place an 'X'")
                        #if x_coordinates not in player_grid:
                            #raise ValueError("Coordinates must be inside the grid, please try again.")
                    #except ValueError as ve:

                x_coordinates = input("Write coordinates for where you want to place an 'X'")

                x_row, x_col = ord(x_coordinates[0]) - ord("A"), int(x_coordinates[1]) - 1

                if 0 <= x_row < len(player_grid) and 0 <= x_col < len(player_grid[0]):
                    player_grid[x_row][x_col] = "X"
                else:
                    print("Invalid coordinates for placing 'X'")

                for row in player_grid:
                    print(row)
            x = False
        elif want_random == 1:
            random_player_ships(player_grid)
            x = False


def random_player_ships(player_grid):
    """ Creates random coordinates for the players ships if wanted """
    for i in range(10):
        

        x_coordniate = random.choice(["A", "B", "C", "D", "E", "F", "G"])
        y_coordniate = random.randint(2, 8)
        random_boat_coordinates = x_coordniate + str(y_coordniate)
            
            
        x_row, x_col = ord(random_boat_coordinates[0]) - ord("A"), int(random_boat_coordinates[1]) - 1

        if 0 <= x_row < len(player_grid) and 0 <= x_col < len(player_grid[0]):
            player_grid[x_row][x_col] = "X"
        else:
            print("Invalid coordinates for placing 'X'")

        for row in player_grid:
            print(row)

    

def counting_boats(player_grid, computer_grid):
    """ Counts the X's placed """
    total_boat_parts = sum(row.count("X") for row in player_grid)
    print(f"The number of boat parts placed is {total_boat_parts}")


def random_boats(computer_grid):
    """ Generates random coordinates for the computer ships start and end coordinates. """
    coordinate_list = []
    for i in range(10):
        
        x_coordniate = random.choice(["A", "B", "C", "D", "E", "F", "G"])
        y_coordniate = random.randint(2, 8)
        random_boat_coordinates = x_coordniate + str(y_coordniate)
        coordinate_list.append(random_boat_coordinates)
        
        x_row, x_col = ord(random_boat_coordinates[0]) - ord("A"), int(random_boat_coordinates[1]) - 1

        if 0 <= x_row < len(computer_grid) and 0 <= x_col < len(computer_grid[0]):
            computer_grid[x_row][x_col] = "X"
        else:
            print("Invalid coordinates for placing 'X'")

        for row in computer_grid:
            print(row)
        print(coordinate_list)
    computer_guess_list = coordinate_list

def generate_answer():
        
        x_coordniate = random.choice(["A", "B", "C", "D", "E", "F", "G"])
        y_coordniate = random.randint(2, 8)
    
def computer_guess(computer_guess_list):
    print(computer_guess_list)

def play_game(computer_guess_list):
    player_right_guess = []
    computer_guess(computer_guess_list)

    #while player_right_guess != coordinate_list:
        #print("Time to play!\n")
        #p_guess = input("Your turn! Write your guess here, write in coordinates!\n")
        

        #if p_guess in coordinate_list:
            #print("You guessed right! The computers turn!")
           # player_right_guess.append(p_guess)
      #  elif p_guess not in coordinate_list:
         #   print("Wrong guess! The computers turn!")
    




def main():
    start_game()
    play_game()


main()

