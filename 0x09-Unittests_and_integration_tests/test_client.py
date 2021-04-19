#!/usr/bin/env python3
"""Test Client File"""
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
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

    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos_url(self, mocked_method):
        """
        -----------------------------
        METHOD: test_public_repos_url
        -----------------------------
        Tests whether the
        """
        expected_payload = {'gh_url': 'example.com'}
        mocked_method.return_value = expected_payload

        gh = GithubOrgClient('google')
        url = gh._public_repos_url

        self.assertEqual(url, expected_payload)
        mocked_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()