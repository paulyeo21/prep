import numpy

class Circuits:
    def howLong(self, connects, costs):
        # 1. build adj_matrix with connects and costs args
        # 2. use floyd-warshall's alg to compute longest paths for all pairs
        # 3. return longest path from adj_matrix
        
        # 1. 
        length = len(connects)
        adj_matrix = numpy.zeros((length, length))
        for i in range(length):
            neighbors = connects[i].split(" ")
            neighbor_costs = costs[i].split(" ")
            for j in range(len(neighbors)):
                if neighbors[j]:
                    adj_matrix[i][int(neighbors[j])] = neighbor_costs[j]
        # print(adj_matrix)
        
        # 2.
        for k in range(length):
            for i in range(length):
                for j in range(length):
                    # print("")
                    # print("i: " + str(i))
                    # print("j: " + str(j))
                    # print("k: " + str(k))
                    if adj_matrix[i][k] and adj_matrix[k][j]:
                        if adj_matrix[i][k] + adj_matrix[k][j] > adj_matrix[i][j]:
                            # print("adj[i][k]: " + str(adj_matrix[i][k]))
                            # print("adj[k][j]: " + str(adj_matrix[k][j]))
                            # print("adj[i][j]: " + str(adj_matrix[i][j]))
                            adj_matrix[i][j] = adj_matrix[i][k] + adj_matrix[k][j]
                            # print(adj_matrix)
        # print(adj_matrix)

        # 3.
        longest = 0
        pair = (0, 0)
        for i in range(length):
            for j in range(length):
                if adj_matrix[i][j] > longest:
                    longest = adj_matrix[i][j]
                    pair = (i, j)
        return pair, longest

circuits = Circuits()
print(circuits.howLong(["1 2", "2", ""], ["5 3", "7", ""]))
print(circuits.howLong(["1 2 3 4 5","2 3 4 5","3 4 5","4 5","5",""], ["2 2 2 2 2","2 2 2 2","2 2 2","2 2","2",""]))
print(circuits.howLong(["1","2","3","","5","6","7",""], ["2","2","2","","3","3","3",""]))
print(circuits.howLong(["","2 3 5","4 5","5 6","7","7 8","8 9","10","10 11 12","11","12","12",""], ["","3 2 9","2 4","6 9","3","1 2","1 2","5","5 6 9","2","5","3",""]))
print(circuits.howLong(["","2 3","3 4 5","4 6","5 6","7","5 7",""], [ "","30 50","19 6 40","12 10","35 23","8","11 20","" ]))
