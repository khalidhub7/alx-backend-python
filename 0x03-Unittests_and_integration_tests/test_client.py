#!/usr/bin/env python3
""" test client.py """
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class Test(unittest.TestCase):
    """ test 'GithubOrgClient' class """

    @parameterized.expand([
        ('google', dict), ('abc', dict)
    ])
    def test_org(self, arg1, expected):
        """ test 'test_org' """
        with patch('client.get_json') as mock_obj:
            mock_obj.return_value = {}
            obj = GithubOrgClient(arg1)

            self.assertEqual(type(obj.org), expected)
            # print(f'*** {obj.__dict__} ***')
            mock_obj.assert_called_once()


if __name__ == '__main__':
    unittest.main()
