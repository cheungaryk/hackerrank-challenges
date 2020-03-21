#!/bin/python3

import unittest

from main import check_weirdness

class TestCheckWeirdness(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        
        # test 1
        n = 1
        result = check_weirdness(n)
        self.assertEqual(result, "Weird")

if __name__ == '__main__':
    unittest.main()