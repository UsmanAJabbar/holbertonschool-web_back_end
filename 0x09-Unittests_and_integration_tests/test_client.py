#!/usr/bin/env python3
"""Test Client File"""
from client import GitHubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock
import unittest


class TestGitHubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, gh_user, mocked_method):
        mocked_method.return_value = [gh_user]
        gh = GitHubOrgClient(gh_user)
        self.assertIn(gh_user, gh.org)
        mocked_method.assert_called_once_with(f'https://api.github.com/orgs/{gh_user}')


if __name__ == '__main__':
    unittest.main()