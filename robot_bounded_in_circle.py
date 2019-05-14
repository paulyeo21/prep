# 1041. Robot Bounded In Circle

# Given a robot that stands north at (0, 0) and instructions to move,
# repeatedly, 'G' go straight one unit, 'L' turn left, and 'R' turn 
# right, find if robot is in a loop.
#
# For instance, if given instructions 'GL' the robot will go to 
# (0, 1) -> then (1, 1) -> then (1, 0) and back to (0, 0). This
# is a loop. so return True

def isRobotBounded(instructions):
    # We know that if at the end of the instructions we are back at
    # (0, 0) we are bounded. If we repeat the instructions and we
    # come back to (0, 0) we also know that we are bounded. How
    # do we know how many times to repeat before realizing we failed?
    # If we take 'GG' we know tht after the second time, we are farther
    # than the first time. For instance, from (0, 2) we go to (0, 4).
    # After four sets of instructions, we will know if its back to (0, 0).
    # If not, then False.

    # iterate four times
    # for each instruction
    # if 'G' and 'N' increment y
    # if 'G' and 'S' decrement y
    # if 'G' and 'W' decrement x
    # if 'G' and 'E' increment x
    # if 'L' and 'N' orientation is 'W'
    # if 'R' and 'N' orientation is 'E'
    # if 'L' and 'W' orientation is 'S'
    # if 'R' and 'W' orientation is 'N'
    # if 'L' and 'S' orientation is 'E'
    # if 'R' and 'S' orientation is 'W'
    # if 'L' and 'E' orientation is 'N'
    # if 'R' and 'E' orientation is 'S'
    x, y = 0, 0
    orientation = 'N'
    for i in range(4):
        # print x, y, orientation
        for instruction in instructions:
            if instruction == 'G':
                if orientation == 'N':
                    y += 1
                elif orientation == 'S':
                    y -= 1
                elif orientation == 'W':
                    x -= 1
                elif orientation == 'E':
                    x += 1
            elif instruction == 'L':
                if orientation == 'N':
                    orientation = 'W'
                elif orientation == 'S':
                    orientation = 'E'
                elif orientation == 'W':
                    orientation = 'S'
                elif orientation == 'E':
                    orientation = 'N'
            elif instruction == 'R':
                if orientation == 'N':
                    orientation = 'E'
                elif orientation == 'S':
                    orientation = 'W'
                elif orientation == 'W':
                    orientation = 'N'
                elif orientation == 'E':
                    orientation = 'S'

    return x == 0 and y == 0

print isRobotBounded('GL') # True
print isRobotBounded('GG') # False
print isRobotBounded('GLGG') # True (0, 0)->(-2, 1)->(-3, -1)->(-1, -2)
