import random


def random_coordinates():
    """ Generates random coordinates for the computer ships start and end coordinates. """
    computer_grid = []

    for x in "ABCDEFG":
        row = [x] + [" "] * 7
        computer_grid.append(row)
    
    # direction_num = random.randint(1, 2)
    direction_num = 2

    random_start_coordinates = ""
    random_end_coordinates = ""
    if direction_num == 1:
        # horizontal
        while random_start_coordinates == random_end_coordinates:
            x_coordniate = random.choice(["A", "B", "C", "D", "E", "F", "G"])
            y_coordniate = random.randint(1, 7)
            random_start_coordinates = x_coordniate + str(y_coordniate)
            
            random_end_coordinates = x_coordniate + str(random.randint(y_coordniate, 7))
            if random_start_coordinates != random_end_coordinates:
                print(random_start_coordinates + " " + random_end_coordinates)

                
    elif direction_num == 2:
        # vertical
        while random_start_coordinates == random_end_coordinates:
            x_coordniate = random.choice(["A", "B", "C", "D", "E", "F", "G"])
            y_coordniate = random.randint(1, 7)
            random_start_coordinates = x_coordniate + str(y_coordniate)
            random_end_coordinates = random.choice(["A", "B", "C", "D", "E", "F", "G"]) + str(y_coordniate)
            
            
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


random_coordinates()