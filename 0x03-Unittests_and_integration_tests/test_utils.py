#!/usr/bin/env python3
""" test utils.py """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
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

            """
            mock_obj.return_value → requests.get
            mock_obj.return_value.json.return_value
                                    → requests.get().json()
            """
            mock_obj.return_value.json.return_value = expected
            result = get_json(arg1)
            self.assertEqual(result, expected)


class TestMemoize(unittest.TestCase):
    """ test 'memoize' """

    def test_memoize(self):
        """ test 'memoize' func """
        class TestClass:
            def a_method(self): return 42

            @memoize
            def a_property(self): return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_obj:
            mock_obj.return_value = 42
            new_obj = TestClass()
            new_obj.a_property, new_obj.a_property
            mock_obj.assert_called_once()


if __name__ == '__main__':
    unittest.main()
