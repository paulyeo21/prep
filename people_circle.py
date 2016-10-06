class PeopleCircle:
    def order(self, numMales, numFemales, k):
        circle = ["M"] * (numMales + numFemales)

        females = []
        index = (k - 1) % len(circle)
        while numFemales > 0:
            index = (index + k) % len(circle)
            circle.pop(index)
            females.append(index)
            numFemales -= 1

        print(circle)
        print(females[::-1])

        previous = females[0]
        for female in (females[1:]):
            index = (female + previous) % len(circle)
            circle = circle[:index] + ["F"] + circle[index:]

        print(circle)

        # return "".join(circle)

people_circle = PeopleCircle()
# print(people_circle.order(5, 3, 2))
# print(people_circle.order(7, 3, 1))
print(people_circle.order(5, 5, 3))
# print(people_circle.order(25, 25, 1000))
