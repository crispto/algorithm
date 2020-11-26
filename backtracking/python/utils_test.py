import unittest
from utils import *


class testUtils(unittest.TestCase):
    graph = [[0, 1, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1],
             [0, 0, 1, 0, 0],
             [1, 0, 0, 1, 0]]

    def test_list_print(self):
        list_print(self.graph)


if __name__ == "__main__":
    unittest.main()
