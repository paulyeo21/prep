def maxStepsUtil(n, k, current_step, current_sequence):
    if current_sequence <= n:
        if k == current_step:
            return
        else:
            return max(maxStepsUtil(n, k, current_step + current_sequence, current_sequence + 1),
                    maxStepsUtil(n, k, current_step, current_sequence + 1))
    else:
        return current_step

def maxSteps(n, k):
    return maxStepsUtil(n, k, 0, 1)

print maxSteps(2, 2) #3
print maxSteps(2, 1) #2
print maxSteps(3, 3) #5
