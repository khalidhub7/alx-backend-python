#!/usr/bin/env python3
"""
unit tests: access_nested_map()
"""
from unittest import TestCase
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json, memoize)
from typing import Dict, Tuple, Union


class TestAccessNestedMap(TestCase):
    """ testcases """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self, nested_map: Dict, path: Tuple[str],
            expected_result: Union[int, Dict]) -> None:
        """ test """
        self.assertEqual(access_nested_map(
            nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(
            self, nested_map: Dict, path: Tuple[str],
            expected_result: str) -> None:
        """ KeyError test for invalid paths """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
            self.assertEqual(
                str(context.exception), expected_result)


class TestGetJson(TestCase):
    """ Test the get_json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(
            self, url, payload, mock_obj):
        """ Test the get_json """
        mock_obj.return_value.json.return_value = payload
        result = get_json(url)
        self.assertEqual(result, payload)
        mock_obj.assert_called_once_with(url)


class TestMemoize(TestCase):
    """ Test memoization decorator """

    def test_memoize(self):
        """ Test a_property """
        class TestClass:
            """ test a_method memoization"""

            def a_method(self):
                """ returns a constant """
                return 42

            @memoize
            def a_property(self):
                """ calls a_method """
                return self.a_method()

        with patch.object(
            TestClass, "a_method",
            return_value=lambda: 42
        ) as mock_a_method:
            obj = TestClass()
            result_1 = obj.a_property()
            result_2 = obj.a_property()

            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)
            mock_a_method.assert_called_once()
