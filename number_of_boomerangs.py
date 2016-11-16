"""
    Given n points in the plane that are all pairwise distinct,
    a "boomerang" is a tuple of points (i, j, k) such that the distance
    between i and j equals the distance between i and k.
    
    Find the number of boomerangs. You may assume that n will be at most
    500 and coordinates of points are all in the range [-1000, 1000] (inclusive).
"""
import math

def distance(point1, point2):
    return math.sqrt( (point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 )

def numberOfBoomerangs(points):
    boomerangs = {}
    for i in range(len(points)):
        current = points[i]
        distances = {}
        # print("Current: ")
        # print(current)

        for j in range(len(points)):
            if i != j:
                dist = distance(current, points[j])
                # print(points[j])
                # print(dist)

                if dist in distances:
                    for point in distances[dist]:
                        boomerang = (i, point, j)
                        if boomerang not in boomerangs:
                            boomerangs[boomerang] = True

                        boomerang = (i, j, point)
                        if boomerang not in boomerangs:
                            boomerangs[boomerang] = True

                    distances[dist].append(j)
                    # print(boomerangs)
                else:
                    distances[dist] = [j]

        # print(distances)
        # print

    return len(boomerangs)

# print(numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))
print(numberOfBoomerangs([[5,5],[4,7],[6,5],[6,9],[3,7],[4,5],[2,5],[4,4],[3,0]]))
