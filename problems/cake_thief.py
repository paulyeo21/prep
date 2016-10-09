def max_duffel_bag_value(cakes, capacity):
    global_max = [0] * (capacity + 1)
    for x in range(1, capacity + 1):
        for cake in cakes:
            weight = cake[0]
            value = cake[1]
            if weight <= x:
                if value + global_max[x - weight] > global_max[x]:
                    global_max[x] = value + global_max[x - weight]
    return global_max[capacity]

cakes = [(7, 160), (3, 90), (2, 15)]
capacity = 20
print(max_duffel_bag_value(cakes, capacity))
