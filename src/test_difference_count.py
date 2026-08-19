import unittest
from difference_count import difference_count_generator

class TestDifferenceCount(unittest.TestCase):

    def test_diff_count_eq(self):
        diff_dict = {
            "application": {
                "version": {
                    "file1_value": "1.0",
                    "file2_value": "2.0"
                },
                "environment": {
                    "file1_value": "prod",
                    "file2_value": "dev"
                }
            }
        }

        missing_keys = {
            "file1": ["features.beta"],
            "file2": ["database.replica", "maintenance"]
        }

        key_count, value_count = difference_count_generator(diff_dict, missing_keys)
        expected_key_count = 3
        expected_value_count = 2

        self.assertEqual(key_count, expected_key_count)
        self.assertEqual(value_count, expected_value_count)

    def test_no_differences(self):
        diff_dict = {}
        missing_keys = {}

        key_count, value_count = difference_count_generator(diff_dict, missing_keys)

        self.assertEqual(key_count, 0)
        self.assertEqual(value_count, 0)

    def test_nested_value_count(self):
        diff_dict = {
            "database": {
                "connection": {
                    "primary": {
                        "host": {
                            "file1_value": "prod-db",
                            "file2_value": "stage-db"
                        }
                    }
                }
            }
        }

        missing_keys = {}

        key_count, value_count = difference_count_generator(diff_dict, missing_keys)

        self.assertEqual(key_count, 0)
        self.assertEqual(value_count, 1)
