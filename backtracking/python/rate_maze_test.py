import unittest

from rate_maze import *


class testValidNext(unittest.TestCase):
    graph = [[0, 1, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1],
             [0, 0, 1, 0, 0],
             [1, 0, 0, 1, 0]]

    # def test_mymax(self):
    #     print(my_max(3, 4))

    def test_valid_pos(self):
        route = [[0 for i in j] for j in self.graph]
        v = valid_next(self.graph, route, [0, 0])
        print(v)


if __name__ == "__main__":
    unittest.main()
