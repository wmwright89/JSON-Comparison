import unittest
from json_compare import start_compare, key_diff_finder, value_diff_finder, verifyJSON

class TestExtract(unittest.TestCase):

    #run test to ensure that the dictionaries are the same
    def test_start_compare_eq(self):
        file1 = "content/config_a.json"
        file2 = "content/config_a.json"

        diff_dict, missing_keys = start_compare(file1, file2)
        expected_diff_dict = {}
        expected_missing_keys = {}
        self.assertEqual(diff_dict, expected_diff_dict)
        self.assertEqual(missing_keys, expected_missing_keys)

    #test to ensure that dictionaries are not the same
    def test_start_compate_not_eq(self):
        file1 = "content/config_a.json"
        file2 = "content/config_b.json"

        result = start_compare(file1, file2)
        self.assertNotEqual(result, True)

    #test to ensure that file path exists
    def test_verifyJSON_true(self):
        file1 = "content/config_a.json"
        file2 = "content/config_a.json"

        result = verifyJSON(file1, file2)
        self.assertEqual(result, True)

    #test exception on file1
    def test_verifyJSON_exception_file1(self):
        file1 = ""
        file2 = "content/config_a.json"

        with self.assertRaises(Exception):
            verifyJSON(file1, file2)
    
    #test exception on file2
    def test_verifyJSON_exception_file2(self):
        file1 = "content/config_a.json"
        file2 = ""

        with self.assertRaises(Exception):
            verifyJSON(file1, file2)

    #test to ensure both dictionaries are returned without changes
    def test_key_diff_finder_eq(self):
        file1 = {"name": "Macho Man", "role": "Professional Wrestler", "title": "Intercontinental Champion"}
        file2 = {"name": "Macho Man", "role": "Professional Wrestler", "title": "Intercontinental Champion"}

        missing_keys = {"file1": [], "file2": []}

        result1, result2, missing_keys = key_diff_finder(file1, file2, missing_keys, path="")
        self.assertEqual(result1, file1)
        self.assertEqual(result2, file2)

    #non-matching keys removed from the returned dicts
    def test_key_diff_finder_stripped_key(self):
        file1 = {"name": "John Cena", "role": "Professional Wrestler", "title": "WWE Heavy Weight Champion", "catch phrase": "You can't see me"}
        file2 = {"name": "Stone Cold Steve Austin", "role": "Professional Wrestler", "title": "WWE Heavy Weight Champion", "catch phrase": "WHAT", "beer": "Yes"}

        missing_keys = {"file1": [], "file2": []}

        result1, result2, missing_keys = key_diff_finder(file1, file2, missing_keys, path="")
        self.assertEqual(result1, file1)
        self.assertEqual(result2, {"name": "Stone Cold Steve Austin", "role": "Professional Wrestler", "title": "WWE Heavy Weight Champion", "catch phrase": "WHAT"})

    #values are the same
    def test_value_diff_finder_eq(self):
        file1 = {"name": "The Undertaker", "role": "Dead Man"}

        result = value_diff_finder(file1, file1)
        self.assertEqual(result, {})

    #values are different
    def test_value_diff_finder_again_eq(self):
        file1 = {"name": "Scott Steiner", "nickname": "Big Poppa Pump", "brother": "Rick Steiner"}
        file2 = {"name": "Scott Steiner", "nickname": "Big Bad Booty Daddy", "brother": "Rick Steiner"}

        result = value_diff_finder(file1, file2)
        expected = {
                "nickname": {
                    "file1_value": "Big Poppa Pump",
                    "file2_value": "Big Bad Booty Daddy"
                    }
                }
        self.assertEqual(result, expected)

    #recusion test for key diff finder
    def test_key_diff_finder_recursion(self):
        file1 = {
            "wrestler": {
                "name": "The Rock",
                "finisher": "The Rock Bottom"
            }
        }

        file2 = {
            "wrestler": {
                "name": "The Rock",
                "finisher": "The Rock Bottom",
                "raised eyebrow": "true"
            }
        }

        missing_keys = {"file1": [], "file2": []}

        result1, result2, missing_keys = key_diff_finder(file1, file2, missing_keys, path="")
        self.assertEqual(result1, file1)
        self.assertEqual(result2, file1)

    #recursion test for value diff finder
    def test_value_diff_finder_recursion(self):
        file1 = {
            "wrestler": {
                "name": "Mick Foley",
                "nickname": "Mankind"
            }
        }

        file2 = {
            "wrestler": {
                "name": "Mick Foley",
                "nickname": "Dude Love"
            }
        }

        missing_keys = {"file1": [], "file2": []}

        result = value_diff_finder(file1, file2)
        expected = {
            "wrestler": {
                "nickname": {
                    "file1_value": "Mankind",
                    "file2_value": "Dude Love"
                }
            }
        }
        
        self.assertEqual(result, expected)
