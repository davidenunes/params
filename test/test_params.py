import unittest
from params import ParamSpace
from params import param_utils

import csv
import os


class MyTestCase(unittest.TestCase):
    def test_param_grid(self):
        ps = ParamSpace()
        ps.add_value("p1", True)
        ps.add_list("p2", ["A", "B"])
        ps.add_random("p3", 0, 1, 3)
        print("param space size ", ps.grid_size)

        print(ps.get_params())
        grid = ps.param_grid()

        for params in grid:
            print(params)

        grid = ps.param_grid()
        grid = list(grid)
        self.assertEqual(len(grid), 1 * 2 * 3)
        self.assertEqual(len(grid), ps.grid_size)

    def test_write_summary(self):
        summary_file = "params.csv"

        ps = ParamSpace()
        ps.add_value("p1", True)
        ps.add_list("p2", ["A", "B"])
        ps.add_random("p3", 0, 1, 3)
        print("param space size ", ps.grid_size)

        ps.write_grid_summary(summary_file)

        written_summary = open(summary_file)
        reader = csv.DictReader(written_summary)

        params = [dict(config) for config in reader]
        print("read parameters")
        for config in params:
            print(config)

        written_summary.close()
        os.remove(summary_file)

        self.assertEqual(len(params), ps.grid_size)

    def test_write_grid_files(self):
        ps = ParamSpace()
        ps.add_value("p1", True)
        ps.add_list("p2", ["A", "B"])
        ps.add_random("p3", 0, 1, 3)
        print("param space size ", ps.grid_size)

        out_path = "/tmp/test_params/"
        if not os.path.exists(out_path) or not os.path.isdir(out_path):
            os.makedirs(out_path)
        param_utils.write_config_files(ps,out_path)





if __name__ == '__main__':
    unittest.main()
