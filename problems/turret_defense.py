class TurretDefense:
    def firstMiss(self, xs, ys, times):
        current_time = 0
        previous = (0, 0)
        for i in range(len(xs)):
            current = (xs[i], ys[i])
            time = self.abs_difference((previous[0], current[0])) + self.abs_difference((current[1], previous[1]))
            if current_time + time <= times[i]:
                current_time = times[i]
                previous = current
            else:
                return i
        return -1

    def abs_difference(self, coordinates):
        return abs(coordinates[0] - coordinates[1])

turret_defense = TurretDefense()
print(turret_defense.firstMiss([3, 5, 6], [7, 5, 6], [11, 15, 16]))
print(turret_defense.firstMiss([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,31]))
