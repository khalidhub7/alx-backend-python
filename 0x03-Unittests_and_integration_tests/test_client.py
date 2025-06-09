#!/usr/bin/env python3
""" test client.py """
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
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

    def test_public_repos_url(self):
        """ test '_public_repos_url' """
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock
                          ) as mock_obj:
            mock_obj.return_value = {'repos_url': 'just testing'}
            obj = GithubOrgClient('google')
            # print(f'*** {obj._public_repos_url} ***')
            self.assertEqual(obj._public_repos_url, 'just testing')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ test 'public_repos' """
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock
                          ) as mock__public_repos_url:

            payload = {
                'repos_url': "https://api.github.com/orgs/google/repos",
                'repos': [
                    {"name": "repo1", "license": {"key": "mit"}},
                    {"name": "repo2", "license": {"key": "apache-2.0"}}
                ]
            }

            # this get repos_url from payload
            mock__public_repos_url.return_value = payload['repos_url']
            # this is payload
            mock_get_json.return_value = payload['repos']

            obj = GithubOrgClient('google')
            self.assertEqual(obj.public_repos(), ['repo1', 'repo2'])

            mock__public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

            # print(f'*** {obj.__dict__} ***')

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, arg1, arg2, expected):
        """ test 'test_has_license' """
        self.assertEqual(GithubOrgClient
                         .has_license(arg1, arg2),
                         expected)


if __name__ == '__main__':
    unittest.main()
