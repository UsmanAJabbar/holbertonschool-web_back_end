#!/usr/bin/env python3
"""Unit testing file"""
import unittest
from parameterized import parameterized
from .utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    --------------------------
    CLASS: TestAccessNestedMap
    --------------------------
    Description:
        Unit test for the access_nested_map
        method from the utils script.
    """

    @parameterized.expand([
        # (input 1, input 2, expected output)
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        ------------------------------
        METHOD: test_access_nested_map
        ------------------------------
        Description:
            Checks whether the access_nested_map returns the
            expected output.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        ----------------------------------------
        METHOD: test_access_nested_map_exception
        ----------------------------------------
        Description:
            Tests whether bad edge cases raise the
            KeyError exception
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    ------------------
    CLASS: TestGetJson
    ------------------
    Description:
        Unit test for the get_json method
        from the utils script.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, expected):
        """
        ---------------------
        METHOD: test_get_json
        ---------------------
        Description:
            Tests the get_json method by checking
            whether it returns the expected output
            for their payloads.
        """
        

if __name__ == '__main__':
    unittest.main()
