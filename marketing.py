import numpy

class Marketing:
    def howMany(self, compete):
        length = len(compete)

        # 1. create adj matrix using compete argument
        adj_matrix = numpy.zeros((length, length))
        for i in range(length):
            neighbors = compete[i].split(" ")
            for neighbor in neighbors:
                if neighbor:
                    adj_matrix[i][int(neighbor)] = adj_matrix[int(neighbor)][i] = 1

        possible_trees = 0
        # print(adj_matrix)

        # 2. dfs to traverse graph for each separate tree
        visited = {}

        for v in range(length):
            stack = []
            stack.append(v)

            if v not in visited:
                visited[v] = True

                while stack:
                    # print(visited)
                    current = stack.pop()
                    for w in range(length):
                        if adj_matrix[current][w] == 1:
                            # print(str(current) + " neighbors " + str(w))
                            if w in visited:
                                if visited[w] == visited[current]:
                                    return -1
                            else:
                                stack.append(w)
                                # mark as visited with opposite value of current
                                visited[w] = not visited[current]
                possible_trees += 1
                # print("")

        return 2**possible_trees
                
marketing = Marketing()
print(marketing.howMany(["1 4", "2", "3", "0", ""]))
print(marketing.howMany(["1", "2", "0"]))
print(marketing.howMany(["1", "2", "3", "0", "0 5", "1"]))
print(marketing.howMany(["", "", "", "", "", "", "", "", "", "",
    "", "", "", "", "", "", "", "", "", "",
    "", "", "", "", "", "", "", "", "", ""]))
print(marketing.howMany(["1", "2", "3", "0", "5", "6", "4"]))
