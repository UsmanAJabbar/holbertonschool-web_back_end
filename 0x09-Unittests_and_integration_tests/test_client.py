#!/usr/bin/env python3
"""Test Client File"""
from client import GitHubOrgClient
from parameterized import parameterized


class TestGitHubOrgClient(unittest.TestCase)

	@parameterized.expand([
		('google'),
		('abc')
	])
    def test_org(self, gh_user):
		