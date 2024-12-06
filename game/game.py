from random import randint  # We import randint to generate random numbers

MINES10 = 10
WIDTH10 = 10
HEIGHT10 = 10

LOSS = False
"""We define values for game width, height and number of mines"""


def generate_field(w, h):
    """generating field, True/False = mine, number = mines around this field, True/False open?"""
    generated = [[[False, 0, False] for i in range(w)] for i in range(h)]
    print("Empty field generated")
    # field_print(generated)
    return generated


def set_mines(num, w, h, field):
    """places mines on the field by changing False to True"""
    check = 0
    mines_list = []
    for i in range(num):
        a = randint(0, w - 1)
        b = randint(0, h - 1)
        while field[b][a][0] is True:
            a = randint(0, w - 1)
            b = randint(0, h - 1)
        mines_list.append(f"{b};{a}")
        field[b][a][0] = True
    # print(f"Mine Locations: {mines_list}")
    print("Mined field generated")
    # field_print(field)
    for j in range(h):
        check = check + int(field[j].count([True, 0, False]))
    print("Minecheck: " + str(check) + " Mines")
    return field


def mine_detection(h, w, field):
    """Detects the number of mines around each field."""
    checklist = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(h):
        for j in range(w):
            x = 0
            for di, dj in checklist:
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w:
                    if field[ni][nj][0] is True:
                        x += 1
            if field[i][j][0] is False:
                field[i][j][1] = x
    print("Detected field generated")
    # field_print(field)
    return field


def field_print(inp):
    """prints readable fields"""
    for i in range(HEIGHT10):
        print(inp[i])


def create_vis_field(h, w):
    """Changes numbers, mines and covered fields with symbols"""
    field = [[] for i in range(h)]
    numbers = ["◻", "①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧"]
    for j in range(h):
        for k in range(w):
            if playfield[j][k][2] is False:
                field[j].append("■")
            if playfield[j][k][2] is True:
                if playfield[j][k][0] is False:
                    field[j].append(numbers[playfield[j][k][1]])
                if playfield[j][k][0] is True:
                    field[j].append("◈")
    return field


def zero_field(h, w, field, list):
    """open all fields around a 0-field and repeat for new 0-fields"""
    checklist = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i, j in checklist:
        if 0 <= j + h < HEIGHT10 and 0 <= i + w < WIDTH10:
            # field_print(field)
            if field[j + h][i + w][2] is False:
                field[j + h][i + w][2] = True
                if field[j + h][i + w][1] == 0:
                    list.append([j + h, i + w])
    # field_print(field)

    return list


def input_check(var, value):
    inp = input(f"{var}: ")
    while True:
        try:
            if 0 <= int(inp) < value:
                return int(inp)
            else:
                inp = input(f"{var}: ")
        except:
            inp = input(f"{var}: ")


def count_open_fields(field):
    x = 0
    for i in range(HEIGHT10):
        for j in range(WIDTH10):
            if field[i][j][2] is True:
                x += 1
    return x


gfield = generate_field(WIDTH10, HEIGHT10)
minefield = set_mines(MINES10, WIDTH10, HEIGHT10, gfield)
playfield = mine_detection(HEIGHT10, WIDTH10, minefield)
field_print(create_vis_field(HEIGHT10, WIDTH10))


def game_loop(field, l):
    """main game-loop"""
    while l is False:
        zero_check = []
        x, y = input_check("x", WIDTH10), input_check("y", HEIGHT10)
        field[y][x][2] = True
        # field_print(field)
        if field[y][x][0] is True:
            l = True
            return l
        if field[y][x][1] == 0 and field[y][x][0] is False:
            zero_check.append([y, x])
        while len(zero_check) > 0:
            zero_check = zero_field(
                zero_check[0][0], zero_check[0][1], field, zero_check
            )
            zero_check.pop(0)
        if count_open_fields(field) == (HEIGHT10 * WIDTH10 - MINES10):
            return l
        field_print(create_vis_field(HEIGHT10, WIDTH10))


LOSS = game_loop(playfield, LOSS)
if LOSS is True:
    print("you hit a mine and lose the game")
if LOSS is False:
    print("you don't hit a mine and win the game")
