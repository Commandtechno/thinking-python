import math


def draw_grid(width, height):
    h_line = ""
    v_line = ""
    q_width = width / 4
    for x in range(width):
        if (
            x == 0
            or x == width - 1
            or x == math.floor(q_width)
            or x == math.floor(q_width * 2)
            or x == math.floor(q_width * 3)
        ):
            h_line += "+ "
            v_line += "| "
        else:
            h_line += "- "
            v_line += "  "

    q_height = height / 4
    for y in range(height):
        if (
            y == 0
            or y == height - 1
            or y == math.floor(q_height)
            or y == math.floor(q_height * 2)
            or y == math.floor(q_height * 3)
        ):
            print(h_line)
        else:
            print(v_line)


draw_grid(21, 21)
