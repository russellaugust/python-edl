# -*- coding: utf-8 -*-

import unittest
import edl
import os
from pathlib import Path

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

class ListTestCase(unittest.TestCase):
    """tests the edl.edl.List class
    """

    def setup(self):
        """set up the tests
        """
        pass

    def test_repr_is_matching_Python_standard(self):
        """testing if the List.__repr__ method output is matching Python
        standard of <edl.edl.List object at 0x??????> format
        """
        self.fail('test is not implemented yet')

    def testing_to_edl_method_will_output_the_standard_edl_case1(self):
        """testing if to_string will output the EDL as string
        """
        p = edl.Parser('24')
        path = os.path.join(THIS_DIR, 'test_data/test_24.edl')
        with open(path) as f:
            s = p.parse(f)

        path = os.path.join(THIS_DIR, 'test_data/test_24.edl')
        with open(path) as f:
            expected_edl = f.readlines()

        self.maxDiff = None

        self.assertEqual(
            ''.join(expected_edl),
            s.to_string()
        )

    def testing_to_edl_method_will_output_the_standard_edl_case2(self):
        """testing if to_string will output the EDL as string
        """
        p = edl.Parser('24')
        path = os.path.join(THIS_DIR, 'test_data/test.edl')
        with open(path) as f:
            s = p.parse(f)

        path = os.path.join(THIS_DIR, 'test_data/test.edl')
        with open(path) as f:
            expected_edl = f.readlines()

        print(s.to_string())

        self.assertEqual(
            ''.join(expected_edl),
            s.to_string()
        )

    def testing_to_edl_method_will_output_the_standard_edl_case3(self):
        """testing if to_string will output the EDL as string
        """
        p = edl.Parser('24')
        path = os.path.join(THIS_DIR, 'test_data/test_50.edl')
        with open(path) as f:
            s = p.parse(f)

        path = os.path.join(THIS_DIR, 'test_data/test_50.edl')
        with open(path) as f:
            expected_edl = f.readlines()

        print(s.to_string())

        self.assertEqual(
            ''.join(expected_edl),
            s.to_string()
        )
