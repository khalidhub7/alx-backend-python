#!/usr/bin/env python3
""" test utils.py """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """ test access_nested_map cases """

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


class TestGetJson(unittest.TestCase):
    """ test 'get_json' """

    @parameterized.expand(
        [
            ('http://example.com', {"payload": True}),
            ('http://holberton.io', {"payload": False})
        ]
    )
    def test_get_json(self, arg1, expected):
        """ test 'get_json' func """
        with patch('requests.get') as mock_obj:

            '''
            mock_obj.return_value → requests.get
            mock_obj.return_value.json.return_value
                                    → requests.get().json()
            '''
            mock_obj.return_value.json.return_value = expected
            result = get_json(arg1)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
