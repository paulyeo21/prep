class DivideJewelry:
    def divide(self, jewelry):
        length = len(jewelry)
        solutions = {}
        for i in range(length - 1):
            # if solutions[jewelry[i]]:
            #     return
            # else:
            #     solutions[jewelry[i]] = [i] 
            solutions[jewelry[i]] = [i] 

            for j in range(i + 1, length):
                solution = jewelry[i] + jewelry[j]
                # if solutions[solution]:
                #     return
                # else:
                #     solutions[solution] = [i, j]
                solutions[solution] = [i, j]

            
        res = [0] * length
        for k in range(length):
            if jewelry[k] in solutions:
                if k not in solutions[jewelry[k]]:
                    res[k] = 1
                    for element in solutions[jewelry[k]]:
                        res[element] = -1
                    return res
        return []


divide_jewelry = DivideJewelry()
print(divide_jewelry.divide([1,2,3]))
print(divide_jewelry.divide([1,2]))
print(divide_jewelry.divide([1,1,2,4,8,16,32]))
print(divide_jewelry.divide([1,2,4,8,16,32]))
# print(divide_jewelry.divide([534,260,643,230,450,560,430,210]))
