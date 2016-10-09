import numpy
import math
from ..data_structures.priority_queue import PriorityQueue

class KiloManX:
    def least_shots(self, damage_chart, boss_health):
        # 1. Create adj matrix with costs being the number of shots it takes to beat a certain boss
        # 2. Use Dijkstra's algorithm to find shortest path (smallest number of shots) finish when number of bosses beaten = number of bosses
        # 3. Return the path cost

        # 1. 
        length = len(damage_chart)
        adj_matrix = numpy.zeros((length + 1, length + 1))

        # Initialize Kilo Buster (starting weapon)
        for i in range(length):
            adj_matrix[0][i + 1] = boss_health[i]
        
        # print(adj_matrix)

        # Now for other weapons
        for i in range(len(damage_chart)):
            boss = boss_health[i]

            for j in range(len(damage_chart[i])):
                if int(damage_chart[i][j]):
                    shots_needed = math.ceil(boss / float(damage_chart[i][j]))
                else:
                    shots_needed = 0
                adj_matrix[i + 1][j + 1] = shots_needed

        # print(adj_matrix)

        # 2.
        frontier = PriorityQueue()
        frontier.put(0, 0)
        cost_so_far = { 0: [ 0, 0 ] } # vertex
        came_from = {}

        while not frontier.empty():
            current = frontier.get()

            if cost_so_far[current][1] == length:
                return cost_so_far[current][0]

            for v in range(length + 1):
                if adj_matrix[current][v]:
                    new_cost = adj_matrix[current][v] + cost_so_far[current][0]

                    # Check if came_from[current] contains v
                    if not self.repeat_boss(came_from, length, current, v) or new_cost < cost_so_far[v][0]:
                        frontier.put(v, new_cost)
                        cost_so_far[v] = [ new_cost, cost_so_far[current][1] + 1 ]
                        came_from[v] = current
    
    def repeat_boss(self, came_from, length, current, key):
        for x in range(length):
            if current in came_from:
                if key == came_from[current]:
                    return True
        return False

kilo_man_x = KiloManX()
print(kilo_man_x.least_shots(["070", "500", "140"], [150, 150, 150]))
print(kilo_man_x.least_shots([ "1542", "7935", "1139", "8882" ], [ 150,150,150,150 ]))
