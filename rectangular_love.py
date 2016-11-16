def rectangular_love(first, second):
    first_x1 = first["left_x"]
    first_x2 = first_x1 + first["width"]
    first_y1 = first["bottom_y"]
    first_y2 = first_y1 + first["height"]

    second_x1 = second["left_x"]
    second_x2 = second_x1 + second["width"]
    second_y1 = second["bottom_y"]
    second_y2 = second_y1 + second["height"]

    # print(first_x1)
    # print(first_x2)
    # print(first_y1)
    # print(first_y2)
    # print(second_x1)
    # print(second_x2)
    # print(second_y1)
    # print(second_y2)

    x_intersects = (first_x1 > second_x2 and first_x1 < second_x1) or \
            (first_x2 > second_x1 and first_x2 < second_x2)

    y_intersects = (first_y1 > second_y2 and first_y1 < second_y1) or \
            (first_y2 > second_y1 and first_y2 < second_y2)

    if x_intersects and y_intersects:
        return True
    else:
        return False

first = {
    'left_x': 1,
    'bottom_y': 5,
    'width': 10,
    'height': 4,
}

second = {
    'left_x': 2,
    'bottom_y': 6,
    'width': 10,
    'height': 4,
}

third = {
    'left_x': 2,
    'bottom_y': 6,
    'width': 10,
    'height': 4,
}

fourth = {
    'left_x': 0,
    'bottom_y': 0,
    'width': 1,
    'height': 1,
}
print(rectangular_love(first, second))
print(rectangular_love(third, second))
print(rectangular_love(third, fourth))
