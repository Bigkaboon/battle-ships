import random

def random_coordinates():
    """ Generates random coordinates for the computer ships start and end coordinates. """
    direction_num = random.randint(1, 2)

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
            


random_coordinates()