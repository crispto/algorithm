from backtracking.python.n_queen import can_attack
import unittest

from .n_queen import can_attack


class TestNQueen(unittest.TestCase):
    def test_can_attach(self):
        cases = [((0, 0), (1, 1), True),
                 ((0, 0), (1, 2), False),
                 ((1, 2), (3, 4), True),
                 ]
        for c in cases:
            self.assertEqual(can_attack(c[0], c[1]), c[2])


if __name__ == "__main__":
    unittest.main()
