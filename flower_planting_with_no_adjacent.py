# 1042. Flower Planting With No Adjacent

# Graph coloring. Given 4 colors and a graph with at most 3 connections
# per node, find a coloring. Graph is given as an edge list. Return 
# an array with [1,2,3,4] as colors and ith index of a garden.
class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

def gardenNoAdj(n, paths):
    # Iterate over each node in the graph, find the colors of the node's
    # neighbors. And use the first color that isn't in the neighbor nodes'
    # set of colors to assign as current node's color. Do this for every
    # node. Need to consider that the relationships given in edge list
    # does not consider bidirection even though the relationships are.
    # For instance, [[1,2],[2,3],[3,1]] has a relationship from
    # 1 -> 2, which means 2 -> 1, but does not show in the edge list. 
    # T: O(n * m) n is number of nodes, m is number of neighbors (max degree)
    # S: O(n)

    # Construct graph from edge list.
    # Iterate over nodes
    # Get set of neighbors colors
    # For each color try to color current node if not in neighbors colors
    # Consider nodes with no edges, cycles, and loops

    graph = [None]

    for i in xrange(1, n + 1):
        graph.append(GraphNode(i))

    for x, y in paths:
        a = graph[x]
        b = graph[y]
        a.neighbors.add(b)
        b.neighbors.add(a)

    colors = [1,2,3,4]

    for node in graph:
        if node:
            if node in node.neighbors:
                raise Exception('Legal coloring impossible for node with loop')

            illegal_colors = set([
                neighbor.color
                for neighbor in node.neighbors
                if neighbor.color
            ])

            for color in colors:
                if color not in illegal_colors:
                    node.color = color
                    break

    output = []
    for node in graph:
        if node:
            output.append(node.color)
    return output

print gardenNoAdj(3, [[1,2],[2,3],[3,1]]) # [1,2,3]
print gardenNoAdj(4, [[1,2],[3,4]]) # [1,2,1,2]
print gardenNoAdj(4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]) # [1,2,3,4]
print gardenNoAdj(3, [[1,2]]) # [1,2,1]
print gardenNoAdj(1, [[1,1]]) # Exception 

