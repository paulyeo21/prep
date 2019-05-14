# Given a graph with nodes represented by a dictionary
# mapping key as node to values as neighbors, find the
# shortest route for any two nodes.

network = {
    'Min': ['William', 'Jayden', 'Omar'],
    'William': ['Min', 'Noam'],
    'Jayden': ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren': ['Jayden', 'Omar'],
    'Amelia': ['Jayden', 'Adam', 'Miguel'],
    'Adam': ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel': ['Amelia', 'Adam', 'Liam', 'Nathan'],
    'Noam': ['Nathan', 'Jayden', 'William'],
    'Omar': ['Ren', 'Min', 'Scott'],
    'Dude': []
}

# When finding the shortest path we want to consider Greedy Best
# First Search and A*. The cost is number of connections so far.
# Starting with our start node, check neighbors and add them to a
# priority queue with the cost being the number of connections so far.
# Have a came_from hash map to store the path taken. Pop the lowest
# cost node in priority queue and check that nodes neighbors. If
# the path to a neighbor has not been visited or the cost is lower
# than previously visited, add to priority queue and change came_from
# path as well. 
# T: O(n + m)
# S: O(n)

from heapq import heappush, heappop

def shortest_route(graph, start, end):
    frontier = []
    heappush(frontier, (0, start))
    cost_so_far = {start: 0}
    came_from = {start: None}

    while len(frontier) > 0:
        cost, current = heappop(frontier)

        if current == end:
            break

        if current in graph:
            for neighbor in graph[current]:
                new_cost = cost + 1
                if neighbor not in came_from or \
                        new_cost < cost_so_far[neighbor]:
                    heappush(frontier, (new_cost, neighbor))
                    cost_so_far[neighbor] = new_cost
                    came_from[neighbor] = current

    output = []
    current = end
    while current:
        if current not in came_from:
            return []
        output.append(current)
        current = came_from[current]

    output.reverse()
    return output

print shortest_route(network, 'Jayden', 'Adam') # ['Jayden', 'Amelia', 'Adam']
print shortest_route(network, 'Omar', 'Dude') # []
print shortest_route(network, 'Jayden', 'Jayden') # ['Jayden']

