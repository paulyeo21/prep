###

def cross_path(path, speed):
    """
    Prompt: Detect whether given an initial speed if you can cross the path 
    that consists of water and land. You can increase your speed by 1, 
    decrease your speed by 1, or not increase or decrease on each movement.

    Arguments:
    path -- Array: an array representation of a path that consists of land "L" and water "W"
    speed -- Int: the starting speed at which you move
    
    Returns:
    outcome -- Boolean: whether it is possible or not to cross the river given the initial speed
    """

    memo = {}
    return cross_path_util(path, speed, 0, memo)

def cross_path_util(path, speed, index, memo):
    if (speed, index) in memo:
        print "*",
        return memo[(speed, index)]
    elif index >= len(path) - 1:
        return True
    elif speed == 0:
        return False
    elif path[index] == "W":
        return False
    else:
        result = cross_path_util(path, speed + 1, index + speed + 1, memo) | \
                 cross_path_util(path, speed - 1, index + speed - 1, memo) | \
                 cross_path_util(path, speed, index + speed, memo)
        memo[(speed, index)] = result
        return result
    
    
path1 = ["L", "L", "W", "L"]
path2 = ["L", "L", "W", "W", "L", "W", "L", "W", "W", "L"]
path3 = ["L", "L", "W", "L", "W", "W", "L", "W", "W", "L"]
assert cross_path(path1, 1) == True
assert cross_path(path2, 1) == False
assert cross_path(path3, 1) == True
