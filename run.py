player_grid = grid_use

computer_grid = grid_use

def clear_console():
    print("\n" * 50)


def start_game():
    user_name = input("Select a username! \n")
    print(f"Hello {user_name}\n")
    grid_use = grids()


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

    


def main():
    start_game()
    


main()