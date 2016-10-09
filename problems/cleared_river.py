def cleared_river(river_array, current, speed):
    if current > -1 and current < len(river_array):
        if river_array[current]:
            cleared_river(river_array, current + speed, speed) \
                or cleared_river(river_array, current + speed + 1, speed + 1) \
                or cleared_river(river_array, current + speed - 1, speed - 1)
        else:
            return False
    elif current > len(river_array):
        return True


print(cleared_river([True, True, True, True, False, False, False, True, False, False, False, False, True], 0, 2))
