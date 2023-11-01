import random

def counting_boats(computer_grid):
    """ Counts the X's placed """
    total_boat_parts = sum(row.count("X") for row in computer_grid)
    print(f"The number of boat parts placed is {total_boat_parts}")
    

def random_coordinates():
    """ Generates random coordinates for the computer ships start and end coordinates. """
    
    total_boat_parts = 0
    computer_grid = []

    for x in "ABCDEFG":
        row = [x] + [" "] * 8
        computer_grid.append(row)
    
        
    direction_num = random.randint(1, 2)
    

    random_start_coordinates = ""
    random_end_coordinates = ""
    if direction_num == 1:
        # horizontal
        while random_start_coordinates == random_end_coordinates:
            x_coordniate = random.choice(["A", "B", "C", "D", "E", "F", "G"])
            y_coordniate = random.randint(2, 8)
            random_start_coordinates = x_coordniate + str(y_coordniate)
                
            random_end_coordinates = x_coordniate + str(random.randint(y_coordniate, 7))
            if random_start_coordinates != random_end_coordinates:
                print(random_start_coordinates + " " + random_end_coordinates)
                    
                start_coordinates = random_end_coordinates
                end_coordinates = random_start_coordinates

                start_x, start_y = ord(end_coordinates[0]) - ord("A"), int(end_coordinates[1]) - 1
                end_x, end_y = ord(start_coordinates[0]) - ord("A"), int(start_coordinates[1]) - 1
                
                for y in range(start_y, end_y + 1):
                    for x in range(start_x, end_x + 1):
                        computer_grid[x][y] = "X"
                for row in computer_grid:
                    print(row) 
                    

                    
    elif direction_num == 2:
        # vertical
        my_list = ["A", "B", "C", "D", "E", "F", "G"]

        while random_start_coordinates == random_end_coordinates:
            x_coordniate = random.choice(my_list)
            y_coordniate = random.randint(2, 8)
            random_start_coordinates = x_coordniate + str(y_coordniate)
            end_x_coordinate = random.choice(my_list)

            index_of_x = my_list.index(x_coordniate)
            index_of_end_x = my_list.index(end_x_coordinate)

            while index_of_end_x < index_of_x:
                end_x_coordinate = random.choice(my_list)
                if index_of_end_x > index_of_x:
                    break

            random_end_coordinates = end_x_coordinate + str(y_coordniate)
                
                
            if random_start_coordinates != random_end_coordinates:
                print(random_start_coordinates + " " + random_end_coordinates)
                    
                start_coordinates = random_end_coordinates
                end_coordinates = random_start_coordinates

                start_x, start_y = ord(end_coordinates[0]) - ord("A"), int(end_coordinates[1]) - 1
                end_x, end_y = ord(start_coordinates[0]) - ord("A"), int(start_coordinates[1]) - 1

                for x in range(start_x, end_x + 1):
                    for y in range(start_y, end_y + 1):
                        computer_grid[x][y] = "X"
                        
                for row in computer_grid:
                    print(row)

                    ### X's wont be shown if start x(G) > end x (A) = no X
    counting_boats(computer_grid)
        
                


random_coordinates()