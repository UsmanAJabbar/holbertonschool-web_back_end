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
        Tests whether the _public_repos_url is
        correctly set and that the memoization
        is also working accordingly.
        """
        expected_payload = {'gh_url': 'example.com'}
        mocked_method.return_value = expected_payload

        gh = GithubOrgClient('google')
        url = gh._public_repos_url

        self.assertEqual(url, expected_payload)
        mocked_method.assert_called_once()
    
    @patch('client.get_json')
    def test_public_repos(self, mocked_get_json):
        """
        -------------------------
        METHOD: test_public_repos
        -------------------------
        Description:
            Tests public repos
        """
        mocked_get_json.return_value = {'get_json':
                                        'some data the API returned'}
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public_repo_urls:
            expected_payload = [{'gh_url': 'example.com'}]
            mocked_public_repo_urls.return_value = expected_payload

            gh = GithubOrgClient('google')
            url = gh._public_repos_url

            self.assertEqual(url, expected_payload)
            mocked_public_repo_urls.assert_called_once()
            mocked_get_json()
            mocked_get_json.assert_called_once()
    
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license"),
        ({"license": {"key": "other_license"}}, "my_license")
    ])
    def test_has_license(self, license, exp_license_key):
        """
        ------------------------
        METHOD: test_has_license
        ------------------------
        Description:
            Checks whether a license_key is present
            in a license object.
        """
        self.assertEqual(GithubOrgClient.has_license(license, exp_license_key),
                         license['license']['key'] == exp_license_key)


if __name__ == '__main__':
    unittest.main()