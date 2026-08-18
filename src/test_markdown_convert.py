import unittest
import tempfile
import os
from markdown_convert import convert_dict_to_markdown, set_md_heading, write_missing_keys

class TestMarkdownConversion(unittest.TestCase):

    def test_markdown_output(self):
        diff_dict = {
            "application": {
                "version": {
                    "file1_value": "2.4.1",
                    "file2_value": "2.5.0"
                }
            }
        }

        missing_keys = {}

        with tempfile.TemporaryDirectory() as temp_dir:
            convert_dict_to_markdown(diff_dict, missing_keys, temp_dir, depth=1)

            output_path = os.path.join(temp_dir, "json_comparison.md")

            with open(output_path, "r") as file:
                result = file.read()

            expected = """# JSON Comparison


## Value Differences

### application

#### version
- file1_value: 2.4.1
- file2_value: 2.5.0"""

        self.assertEqual(result, expected)

    def test_multiple_comparison_sections(self):
        diff_dict = {
            "application": {
                "environment": {
                    "file1_value": "production",
                    "file2_value": "staging"
                }
            },
            "server": {
                "port":{
                    "file1_value": 443,
                    "file2_value": 8443
                }
            },
            "allowed_regions": {
                "file1_value": ["us-east-1", "us-west-2", "us-west-1"],
                "file2_value": ["us-east-1", "us-west-2"]
            }
        }

        missing_keys = {}
        

        with tempfile.TemporaryDirectory() as temp_dir:
            convert_dict_to_markdown(diff_dict, missing_keys, temp_dir, depth=1)

            output_path = os.path.join(temp_dir, "json_comparison.md")

            with open(output_path, "r") as file:
                result = file.read()

            expected = """# JSON Comparison


## Value Differences

### application

#### environment
- file1_value: production
- file2_value: staging

### server

#### port
- file1_value: 443
- file2_value: 8443

### allowed_regions
- file1_value:
  - us-east-1
  - us-west-2
  - us-west-1
- file2_value:
  - us-east-1
  - us-west-2"""

        self.assertEqual(result, expected)


    def test_missing_keys(self):
        missing_keys = {
            "file1": ["database.read_replica_enabled", "features.enable_new_search"],
            "file2": ["features.enable_dashboard"]
        }
        
        with tempfile.TemporaryDirectory() as temp_dir: 

            output_path = os.path.join(temp_dir, "json_comparison.md")

            write_missing_keys(missing_keys, output_path, depth=3)

            with open(output_path, "r") as file:
                result = file.read()

            expected ="""

### Missing from file1
- database.read_replica_enabled
- features.enable_new_search

### Missing from file2
- features.enable_dashboard"""

        self.assertEqual(result, expected)
