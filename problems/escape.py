import numpy
from ..data_structures.priority_queue import PriorityQueue

class Escape:
    def lowest(self, harmful, deadly):
        # 1. Build adjacency matrix
        #       Mark harmful regions as 1
        #       Mark deadly regions as None(?)
        # 2. Use dijkstra's algorithm to reach from (0, 0) to (500, 500) with least amount of life shed

        # 1.
        adj_matrix = numpy.zeros((501, 501))
        for region in harmful:
            x1, y1, x2, y2 = region.split(" ")
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    adj_matrix[x, y] = 1

        # print(adj_matrix)

        for region in deadly:
            x1, y1, x2, y2 = region.split(" ")
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    adj_matrix[x, y] = -1

        # print(adj_matrix)
        # hacky way to keep start at 0
        adj_matrix[0, 0] = 0

        # 2.
        frontier = PriorityQueue()
        frontier.put((0, 0), 0)
        cost_so_far = {}
        cost_so_far[(0, 0)] = 0
        came_from = {}

        while not frontier.empty():
            x, y = frontier.get()

            if x == 500 and y == 500:
                break
            
            # append each neighbor with new cost to queue
            for neighbor in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:

                if neighbor[0] < 0 or neighbor[0] > 500 or neighbor[1] < 0 or neighbor[1] > 500:
                    continue

                if adj_matrix[neighbor[0], neighbor[1]] < 0:
                    continue

                new_cost = cost_so_far[(x, y)] + adj_matrix[neighbor[0], neighbor[1]]
                
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    frontier.put(neighbor, new_cost)
                    cost_so_far[neighbor] = new_cost
                    came_from[neighbor] = (x, y)

        # print(cost_so_far)
        return cost_so_far[(500, 500)]

escape = Escape()
# print(escape.lowest([], []))
# print(escape.lowest(["500 0 0 500"], ["0 0 0 0"]))
# print(escape.lowest(["0 0 250 250","250 250 500 500"], [ "0 251 249 500","251 0 500 249"]))
# print(escape.lowest(["468 209 456 32",
#  "71 260 306 427",
#  "420 90 424 492",
#  "374 253 54 253",
#  "319 334 152 431",
#  "38 93 204 84",
#  "246 0 434 263",
#  "12 18 118 461",
#  "215 462 44 317",
#  "447 214 28 475",
#  "3 89 38 125",
#  "157 108 138 264",
#  "363 17 333 387",
#  "457 362 396 324",
#  "95 27 374 175",
#  "381 196 265 302",
#  "105 255 253 134",
#  "0 308 453 55",
#  "169 28 313 498",
#  "103 247 165 376",
#  "264 287 363 407",
#  "185 255 110 415",
#  "475 126 293 112",
#  "285 200 66 484",
#  "60 178 461 301",
#  "347 352 470 479",
#  "433 130 383 370",
#  "405 378 117 377",
#  "403 324 369 133",
#  "12 63 174 309",
#  "181 0 356 56",
#  "473 380 315 378"],
# ["250 384 355 234",
#  "28 155 470 4",
#  "333 405 12 456",
#  "329 221 239 215",
#  "334 20 429 338",
#  "85 42 188 388",
#  "219 187 12 111",
#  "467 453 358 133",
#  "472 172 257 288",
#  "412 246 431 86",
#  "335 22 448 47",
#  "150 14 149 11",
#  "224 136 466 328",
#  "369 209 184 262",
#  "274 488 425 195",
#  "55 82 279 253",
#  "153 201 65 228",
#  "208 230 132 223",
#  "369 305 397 267",
#  "200 145 98 198",
#  "422 67 252 479",
#  "231 252 401 190",
#  "312 20 0 350",
#  "406 72 207 294",
#  "488 329 338 326",
#  "117 264 497 447",
#  "491 341 139 438",
#  "40 413 329 290",
#  "148 245 53 386",
#  "147 70 186 131",
#  "300 407 71 183",
#  "300 186 251 198",
#  "178 67 487 77",
#  "98 158 55 433",
#  "167 231 253 90",
#  "268 406 81 271",
#  "312 161 387 153",
#  "33 442 25 412",
#  "56 69 177 428",
#  "5 92 61 247"]))
