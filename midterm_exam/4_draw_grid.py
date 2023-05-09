import math


def draw_grid(width, height):
    h_line = ""
    v_line = ""
    for x in range(width):
        if x == 0 or x == width - 1 or x == math.floor(width / 2):
            h_line += "+ "
            v_line += "| "
        else:
            h_line += "- "
            v_line += "  "

    for y in range(height):
        if y == 0 or y == height - 1 or y == math.floor(width / 2):
            print(h_line)
        else:
            print(v_line)


draw_grid(11, 11)
