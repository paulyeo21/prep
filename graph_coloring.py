# Given an undirected graph, with maximum degree D,
# find a graph coloring using at most D + 1 colors.

class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

def find_graph_coloring(graph, maximum_degree):
    # DFS
    # For each node track neighbors colors. For color(s) that
    # doesn't exist mark current node as one of those colors. 
    # T: O(n)
    # S: O(h)
    visited = set()
    frontier = [graph[0]]
    colors = range(1, maximum_degree + 1) #['red', 'blue', 'green']

    while len(frontier) > 0:
        current = frontier.pop()

        if current not in visited:

            neighbors_colors = set()
            for neighbor in current.neighbors:
                if neighbor.color:
                    neighbors_colors.add(neighbor.color)

                if neighbor not in visited:
                    frontier.append(neighbor)

            for color in colors:
                if color not in neighbors_colors:
                    current.color = color
                    break

            visited.add(current)

    return map(lambda node : (node.label, node.color), graph)


# T: O(n + m) where n is nodes and m is vertices (we cross 2m edges, 
#             because when we iterate over a nodes neighbors, we are
#             looking at a -> b and b -> a.
# S: O(d) where d is maximum degree
def color_graph(graph, colors):
    for node in graph:
        if node in node.neighbors:
            raise Exception('Legal coloring impossible with loop: %s' \
                    % node.label)

        illegal_colors = set([
            neighbor.color
            for neighbor in node.neighbors
            if neighbor.color
        ])

        for color in colors:
            if color not in illegal_colors:
                node.color = color
                break

a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')
d = GraphNode('d')

a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)
c.neighbors.add(d)
d.neighbors.add(a)

print find_graph_coloring([a, b, c, d], 2)
color_graph([a, b, c, d], ['red', 'blue'])
print map(lambda x: (x.label, x.color), [a, b, c, d])
