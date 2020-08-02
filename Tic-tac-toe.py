def check_win_X():
    horizontal_cels = [[field_for_game[0][2], field_for_game[1][2], field_for_game[2][2]],
                       [field_for_game[0][1], field_for_game[1][1], field_for_game[2][1]],
                       [field_for_game[0][0], field_for_game[1][0], field_for_game[2][0]]]
    X_cels = [[field_for_game[0][2], field_for_game[1][1], field_for_game[2][0]],
              [field_for_game[2][2], field_for_game[1][1], field_for_game[0][0]]]

    if ['X', 'X', 'X'] in field_for_game:

        print("X wins")
        return True

    elif ['X', 'X', 'X'] in horizontal_cels:

        print("X wins")
        return True
    elif ['X', 'X', 'X'] in X_cels:

        print("X wins")
        return True
    else:
        return False


def check_win_O():
    horizontal_cels = [[field_for_game[0][2], field_for_game[1][2], field_for_game[2][2]],
                       [field_for_game[0][1], field_for_game[1][1], field_for_game[2][1]],
                       [field_for_game[0][0], field_for_game[1][0], field_for_game[2][0]]]
    X_cels = [[field_for_game[0][2], field_for_game[1][1], field_for_game[2][0]],
              [field_for_game[2][2], field_for_game[1][1], field_for_game[0][0]]]

    if ['O', 'O', 'O'] in field_for_game:

        print("O wins")
        return True
    elif ['O', 'O', 'O'] in horizontal_cels:

        print("O wins")
        return True
    elif ['O', 'O', 'O'] in X_cels:

        print("O wins")
        return True
    else:
        return False


def check_draw():
    global turn
    if turn < 10:
        turn += 1
        return False
    else:
        print("Draw")
        return True


def X_or_O():
    global X_or_O_count
    if X_or_O_count % 2 == 1:
        X_or_O_count += 1
        return "X"
    else:
        X_or_O_count += 1
        return "O"


def field():
    print("""
---------
| {0} {1} {2} |
| {3} {4} {5} |
| {6} {7} {8} |
---------
""".format(field_for_game[0][2],
           field_for_game[1][2],
           field_for_game[2][2],
           field_for_game[0][1],
           field_for_game[1][1],
           field_for_game[2][1],
           field_for_game[0][0],
           field_for_game[1][0],
           field_for_game[2][0], ))


turn = 0
X_or_O_count = 1
numbers = [1, 2, 3]
X_O = ["X", "O"]
field_for_game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

field()

while not (check_win_X() or check_win_O() or check_draw()):

    coordinates = input("Enter the coordinates: ").split()

    if len(coordinates[0]) != 1 or len(coordinates[1]) != 1:
        print("You should enter numbers!")

    elif (int(coordinates[0]) < 1 or int(coordinates[0]) > 3) or (
            int(coordinates[1]) < 1 or int(coordinates[1]) > 3):
        print("Coordinates should be from 1 to 3!")

    elif field_for_game[int(coordinates[0]) - 1][int(coordinates[1]) - 1] in X_O:
        print("This cell is occupied! Choose another one!")

    else:
        field_for_game[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = X_or_O()
        field()
