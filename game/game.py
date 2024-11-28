from random import randint '''We import randint to generate random numbers'''

MINES = 10
WIDTH = 10
HEIGHT = 10
'''We define values for game width, height and number of mines'''


def generate_field(x, y):
    """generating blank field, True/False = mine, number = mines around this field"""
    field = [[[(False), 0] for i in range(x)] for i in range(y)]
    print(field)
    return field

