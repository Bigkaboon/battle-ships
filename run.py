import random

def clear_console():
    """ clearing console once needed """
    print("\n" * 50)


def start_game():
    """ Function for setting up the game """
    user_name = input("Select a username! \n")
    print(f"Hello {user_name}\n")
    grid_use = grids()
    player_grid = grid_use
    computer_grid = grid_use
    clear_console()
    place_comp_ships(computer_grid)
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

    

    grid_type_num = int(input("What grid size would you like to play on \n1. EASY : 7x7 \n2. MEDIUM : 9x9 \n3. HARD : 12x12 \nAnswer with a number 1-3 \n"))
    
    if grid_type_num == 1:
        return grid_1
    elif grid_type_num == 2:
        return grid_2
    elif grid_type_num == 3:
        return grid_3


def place_ships(player_grid):
    """ Lets the user place X's representing the ships """
    for i in range(3):

        for row in player_grid:
            print(row)

        boat_direction = input("What direction do you want the boat to go 'vertical' or 'horizontal'?")
        
        if boat_direction == "vertical":
            print("Place the boat vertically!")
            start_coordinates = input("Write coordinates for where you want the boat to start")
            end_coordinates = input("Write coordinates for where you want the boat to end")

            start_x, start_y = ord(end_coordinates[0]) - ord("A"), int(end_coordinates[1]) - 1
            end_x, end_y = ord(start_coordinates[0]) - ord("A"), int(start_coordinates[1]) - 1

            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    player_grid[x][y] = "X"
                
            for row in player_grid:
                print(row)
            
            counting_boats(player_grid)
        elif boat_direction == "horizontal":
            print("Place the boat Horizontally!")
            start_coordinates = input("Write coordinates for where you want the boat to start")
            end_coordinates = input("Write coordinates for where you want the boat to end")

            start_x, start_y = ord(end_coordinates[0]) - ord("A"), int(end_coordinates[1]) - 1
            end_x, end_y = ord(start_coordinates[0]) - ord("A"), int(start_coordinates[1]) - 1
        
            for y in range(start_y, end_y + 1):
                for x in range(start_x, end_x + 1):
                    player_grid[x][y] = "X"
            for row in player_grid:
                print(row) 
    
            counting_boats(player_grid)
              
                
def counting_boats(player_grid):
    """ Counts the X's placed """
    total_boat_parts = sum(row.count("X") for row in player_grid)
    print(f"The number of boat parts placed is {total_boat_parts}")


def random_coordinates():
    """ Generates random coordinates for the computer ships start and end coordinates. """
    direction_num = random.randint(1, 2)

    if direction_num == 1:
        # horizontal
        x_coordniate = random.choice(["A", "B", "C", "D", "E", "F", "G"])
        y_coordniate = random.randint(1, 7)
        random_start_coordinates = x_coordniate + str(y_coordniate)
        print(random_start_coordinates)
        random_end_coordinates = x_coordniate + random.randint(y_coordniate, 7)
    elif direction_num == 2:
        # vertical
        x_coordniate = random.choice(["A", "B", "C", "D", "E", "F", "G"])
        y_coordniate = random.randint(1, 7)
        random_start_coordinates = x_coordniate + str(y_coordniate)
        random_end_coordinates = str(y_coordniate) + random.choice(["A", "B", "C", "D", "E", "F", "G"])
        print(random_start_coordinates)
        print(random_end_coordinates)
def place_comp_ships(computer_grid,):
    random_coordinates()
    for row in computer_grid:
        print(row)


def main():
    start_game()


main()