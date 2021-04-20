#!/usr/bin/env python3
"""Unit testing file"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


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
    @patch('utils.requests.get')
    def test_get_json(self, url, expected_payload, mock_get):
        """
        ---------------------
        METHOD: test_get_json
        ---------------------
        Description:
            Tests the get_json method by checking
            whether it returns the expected output
            for their payloads.
        """
        # Create a mock object that mimics the original dir of .get func
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = expected_payload

        # Now get a response from the actual server
        live_json = get_json(url)

        self.assertEqual(live_json, expected_payload)


class TestMemoize(unittest.TestCase):
    """
    ------------------
    CLASS: TestMemoize
    ------------------
    """

    def test_memoize(self):
        """
        --------------------
        METHOD: test_memoize
        --------------------
        Description:
            Tests whether the memoization is actually
            working by ensuring the method isn't called
            twice.
        """

        class TestClass:
            """
            ----------------
            CLASS: TestClass
            ----------------
            """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                self.a_method()

        with patch.object(TestClass, 'a_method') as mocked_a_method:
            test = TestClass()
            test.a_property
            test.a_property
            mocked_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
