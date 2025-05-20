from random import randint  # We import randint to generate random numbers
import string  # Für die Buchstaben a-z


"""We define values for game width, height and number of mines"""


def size_question():
    while True:
        preset = [[10, 10, 10], [20, 15, 20], [25, 20, 25]]  # w, h, m
        mss = "[1] 10x10 (10 Minen)\n[2] 20x15 (20 Minen)\n[3] 25x20 (25 Minen)\n[4] Custom\nAwnser: "
        awns = int(input_check(mss, "n", 1, 1)) - 1
        if 0 <= awns <= 2:
            w, h, m = preset[awns][0], preset[awns][1], preset[awns][2]
            return w, h, m
        if awns == 3:
            w = int(input_check("Width: ", "n", 1, "i"))
            while w < 10:
                w = int(input_check("Width is too small: ", "n", 1, "i"))
            h = int(input_check("Heigth: ", "n", 1, "i"))
            while h < 10:
                h = int(input_check("Height is too small: ", "n", 1, "i"))
            m = int(input_check("Mines: ", "n", 1, "i"))
            while m < 10 or m > 2 * h * w:
                m = int(input_check("Mines is too small: ", "n", 1, "i"))
            return w, h, m


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
    """Prints the field with row labels (a, b, ...) and column numbers (1, 2, ...)."""
    # Zahlen als Kopfzeile
    header = "   " + " ".join(str(i + 1) for i in range(len(inp[0])))
    print(header)

    # Spielfeld mit Buchstaben links ausgeben
    for index, row in enumerate(inp):
        row_label = string.ascii_lowercase[index]  # Buchstaben a, b, c, ...
        print(f"{row_label}  " + " ".join(row))


def create_vis_field(h, w):
    """Changes numbers, mines and covered fields with symbols"""
    field = [[] for i in range(heigth)]
    numbers = ["◻", "1", "2", "3", "4", "5", "6", "7", "8"]
    for j in range(heigth):
        for k in range(width):
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


def count_open_fields(field, heigth, width):
    x = 0
    for i in range(HEIGHT10):
        for j in range(WIDTH10):
            if field[i][j][2] is True:
                x += 1
    return x


def input_check(
    message, req, length_min, length_max
):  # req can be "n", "a", "an", "anf" (numeric, alphabetic, alphanumeric, alphanumeric force -> at least one alpha and numeric); length is the required length, can also be infinite ("i")
    if req == "n":
        while True:
            inp = input(message)
            if inp.isnumeric() and check_inp_size(inp, length_min, length_max):
                return inp
    elif req == "a":
        while True:
            inp = input(message)
            if inp.isalpha() and check_inp_size(inp, length_min, length_max):
                return inp
    elif req == "an":
        while True:
            inp = input(message)
            if inp.isalnum() and check_inp_size(inp, length_min, length_max):
                return inp
    elif req == "anf":
        while True:
            inp = input(message)
            if (
                inp.isalnum()
                and check_inp_size(inp, length_min, length_max)
                and not (inp.isnumeric() or inp.isalpha())
            ):
                return inp


def check_inp_size(inp, mini, maxi):
    if mini == "i" and not maxi == "i":
        if len(inp) <= maxi:
            return True
    elif maxi == "i" and not mini == "i":
        if len(inp) >= mini:
            return True
    elif mini == "i" and maxi == "i":
        return True
    elif not (mini == "i" or maxi == "i"):
        if mini <= len(inp) <= maxi:
            return True


def let_to_num(miniy, maxiy, minix, maxix):
    while True:
        mss = "Field: "

        let, numb = char_split(input_check(mss, "anf", 2, "i"))
        xw = int(numb) - 1  # z. B. "1" wird zu 0, "2" zu 1
        yh = 0
        for i in let:
            yh = yh * 26 + (ord(i.lower()) - ord("a") + 1)
        yh = yh - 1
        if miniy <= yh <= maxiy and minix <= xw <= maxix:
            return xw, yh


def char_split(inp):
    inp = inp.strip()
    letters = ""
    numbers = ""
    for i in inp:
        if i.isalpha():
            letters += i
        elif i.isdigit():
            numbers += i

    return letters, numbers


def continue_play(mss, width, heigth, field):
    print(mss)
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
