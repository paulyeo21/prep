def upvotes(n, k, upvotes):
    for i in range(n):
        print("i: " + str(i))

        if i + k <= n:
            for j in range(i, k+i):
                print("Range: " + str(i) + " " + str(j))
                # current = upvotes[i + j]

print(upvotes(5, 3, [1, 2, 3, 1, 1]))
