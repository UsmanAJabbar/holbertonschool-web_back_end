#!/usr/bin/env python3
"""Test Client File"""
from client import GitHubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock
import unittest


class TestGitHubOrgClient(unittest.TestCase):
    """
    ------------------
    CLASS:
    -----------------
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, gh_user, mocked_method):
        """"METHOD FOR SOME REASON """
        mocked_method.return_value = {gh_user:True}
        gh = GitHubOrgClient(gh_user)

        test_url = gh.ORG_URL.format(org=gh._org_name)

        self.assertEqual(gh.org, {gh_user:True})
        mocked_method.assert_called_once_with(test_url)


if __name__ == '__main__':
    unittest.main()