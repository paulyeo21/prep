# Given a 2d array find the number of islands

def numberOfIslands(graph):
    islands = 0
    for i in range(len(graph[0])):
        for j in range(len(graph)):
            if (graph[i][j] == 1):
                dfs(graph, i, j, len(graph[0]), len(graph))
                islands += 1
    return islands

def dfs(graph, x, y, width, height):
    graph[x][y] = 0
    if (x + 1 < width):
        if (graph[x + 1][y] == 1):
            graph[x + 1][y] = 0
            dfs(graph, x + 1, y, width, height)
    elif (x - 1 > 0):
        if (graph[x - 1][y] == 1):
            graph[x - 1][y] = 0
            dfs(graph, x - 1, y, width, height)
    elif (y + 1 > height):
        if (graph[x][y + 1] == 1):
            graph[x][y + 1] = 0
            dfs(graph, x, y + 1, width, height)
    elif (y - 1 > 0):
        if (graph[x][y - 1] == 1):
            graph[x][y - 1] = 0
            dfs(graph, x, y - 1, width, height)

assert numberOfIslands([[1, 0, 0], [1, 0, 1], [0, 1, 0]]) == 3
