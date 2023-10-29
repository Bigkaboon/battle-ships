import random

def clear_console():
    """ clearing console once needed """
    print("\n" * 50)


def start_game():
    """ Function for setting up the game """
    user_name = input("Select a username! \n")
    print(f"Hello {user_name}\n")
    grid_use = grids()
    clear_console()
    place_ships(grid_use)
    
    
    

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
    while grid_type_num < 3:
        if grid_type_num == 1:
            return grid_1
        elif grid_type_num == 2:
            return grid_2
        elif grid_type_num == 3:
            return grid_3


def place_ships(grid_use):
    """ Lets the user place X's representing the ships """
    for row in grid_use:
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
                grid_use[x][y] = "X"
            
        for row in grid_use:
            print(row)
        
        counting_boats(grid_use)
         
    elif boat_direction == "horizontal":
        print("Place the boat Horizontally!")
        start_coordinates = input("Write coordinates for where you want the boat to start")
        end_coordinates = input("Write coordinates for where you want the boat to end")

        start_x, start_y = ord(end_coordinates[0]) - ord("A"), int(end_coordinates[1]) - 1
        end_x, end_y = ord(start_coordinates[0]) - ord("A"), int(start_coordinates[1]) - 1
     
        for y in range(start_y, end_y + 1):
            for x in range(start_x, end_x + 1):
                grid_use[x][y] = "X"
        for row in grid_use:
            print(row) 
  
        counting_boats(grid_use)
        
                
def counting_boats(grid_use):
    """ Counts the X's placed """
    total_boat_parts = sum(row.count("X") for row in grid_use)
    print(f"The number of boat parts placed is {total_boat_parts}")


def random_start_coordinates():
    """ Generates random coordinates for the computer ships start and end coordinates. """
    x_coordniate = random.choice(["A", "B", "C", "D", "E", "F", "G"])
    print(x_coordniate)
    y_coordniate = random.randint(1, 7)
    print(y_coordniate)


def main():
    start_game()
    

main()