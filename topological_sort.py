class Solution:
    def __init__(self, graph):
        self.output = []
        self.graph = graph
        self.visited = {}

    def visit(self, node):
        if node in self.visited:
            return
        else:
            self.visited[node] = True
            for neighbor in graph[node]:
                self.visit(neighbor)
            self.output.insert(0, node)

    def topological_sort(self):
        for current, neighbors in graph.iteritems():
            if current in self.visited:
                continue
            else:
                self.visit(current)

        return self.output

graph = {
    2: [],
    3: [10, 11],
    5: [8],
    7: [8, 11],
    8: [2, 9, 10],
    9: [],
    10: [],
    11: [9]
}
solution = Solution(graph)
print(solution.topological_sort())
