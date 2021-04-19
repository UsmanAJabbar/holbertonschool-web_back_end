#!/usr/bin/env python3
"""Test Client File"""
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """
    --------------------------
    CLASS: TestGitHubOrgClient
    --------------------------
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mocked_method):
        """ Tests whether get_json is behaving expectedly """
        mocked_method.return_value = {org_name:True}
        gh = GithubOrgClient(org_name)

        self.assertEqual(gh.org, {org_name:True})
        mocked_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()