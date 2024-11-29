from random import randint  # We import randint to generate random numbers

MINES = 10
WIDTH10 = 10
HEIGHT9 = 9

"""We define values for game width, height and number of mines"""


def generate_field(x, y):
    """generating blank field, True/False = mine, number = mines around this field"""
    generated = [[[(False), 0] for i in range(x)] for i in range(y)]
    print(generated)
    return generated


def set_mines(num):
    """places mines on the field by changing False to True"""
    check = 0
    for i in range(num):
        a = randint(0, WIDTH10 - 1)
        b = randint(0, HEIGHT9 - 1)
        while field[b][a][0] is True:
            a = randint(0, WIDTH10 - 1)
            b = randint(0, HEIGHT9 - 1)
        print(a, b)
        field[b][a][0] = True
    print(field)
    for j in range(10):
        check = check + int(field[j].count([True, 0]))
    print(check)
    return field


def mine_detection():
    """we detect the place of the block and detect if its on top bot etc."""
    for i in range(HEIGHT9):
        for j in range(WIDTH10):
            if i != 0:
                print("not top")
            if i != HEIGHT9 - 1:
                print("not bot")
            if j != 0:
                print("not left")
            if j != WIDTH10 - 1:
                print("not right")

    print("1")


field = generate_field(WIDTH10, HEIGHT9)
minefield = set_mines(MINES)
