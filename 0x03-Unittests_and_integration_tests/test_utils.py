#!/usr/bin/env python3
"""
unit tests: access_nested_map()
"""
from unittest import TestCase
from parameterized import parameterized
from required.utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """ testcases """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ test """
        TestCase.assertEqual(access_nested_map(nested_map, path), expected_result)
