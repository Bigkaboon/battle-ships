

def clear_console():
    print("\n" * 50)


def start_game():
    user_name = input("Select a username! \n")
    print(f"Hello {user_name}\n")
    grid_use = grids()
    clear_console()
    place_ships(grid_use)
    
    

def grids():
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
    


""" def set_grid(grid_use):
    player_grid = grid_use
    computer_grid = grid_use
     """

def place_ships(grid_use):
    for row in grid_use:
        print(row)

    boat_dircetion = "horizontal"

    if boat_dircetion == "vertical":
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
         
    elif boat_dircetion == "horizontal":
        start_coordinates = input("Write coordinates for where you want the boat to start")
        end_coordinates = input("Write coordinates for where you want the boat to end")

        start_x, start_y = ord(end_coordinates[0]) - ord("A"), int(end_coordinates[1]) - 1
        end_x, end_y = ord(start_coordinates[0]) - ord("A"), int(start_coordinates[1]) - 1
     
        for y in range(start_y, end_y + 1):
            for x in range(start_x, end_x + 1):
                grid_use[x][y] = "X"
        for row in grid_use:
            print(row) 
        
                
    



def main():
    start_game()
    

main()