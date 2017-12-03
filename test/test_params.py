import unittest
from params import ParamSpace
import contextlib


class MyTestCase(unittest.TestCase):
    def test_param_grid(self):
        ps = ParamSpace()
        ps.add_value("p1", True)
        ps.add_list("p2", ["A", "B"])
        ps.add_random("p3", 0, 1, 3)
        print("param space size ", ps.grid_size)


        grid = ps.param_grid()


        for params in grid:
            print(params)

        grid = ps.param_grid()
        grid = list(grid)
        self.assertEqual(len(grid), 1 * 2 * 3)
        self.assertEqual(len(grid), ps.grid_size)






if __name__ == '__main__':
    unittest.main()
