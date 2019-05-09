# Given a list of unsorted scores and the highest possible score,
# return a sorted list of scores in less than O(n lg n) time.

# counting sort
# T: O(n + k)
# S: O(n + k)
def sort_scores(unsorted_scores, highest_score):
    counts = [0] * (highest_score + 1)
    output = []

    for score in unsorted_scores:
        counts[score] += 1

    # counts = [1, 1, 2]
    for score in xrange(highest_score, -1, -1):
        for time in xrange(counts[score]):
            output.append(score)

    return output

print sort_scores([3, 3, 1, 2], 3) # [1, 2, 3, 3]
print sort_scores([37, 89, 41, 65, 91, 53], 100) # [91, 89, 65, 53, 41, 37]
