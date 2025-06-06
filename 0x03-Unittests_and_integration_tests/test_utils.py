#!/usr/bin/env python3
""" test utils.py """
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ test funcs """
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(
            self, arg1, arg2, expected):
        """ test 'access_nested_map' """
        self.assertEqual(
            access_nested_map(arg1, arg2), expected
        )

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError)
        ]
    )
    def test_access_nested_map_exception(
            self, arg1, arg2, expected):
        """ test 'access_nested_map' exception """
        with self.assertRaises(expected):
            access_nested_map(arg1, arg2)


if __name__ == '__main__':
    unittest.main()
