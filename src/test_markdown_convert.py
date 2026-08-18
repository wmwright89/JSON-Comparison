import unittest
import tempfile
import os
from markdown_convert import convert_dict_to_markdown, set_md_heading

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

        with tempfile.TemporaryDirectory() as temp_dir:
            convert_dict_to_markdown(diff_dict, temp_dir, depth=1)

            output_path = os.path.join(temp_dir, "json_comparison.md")

            with open(output_path, "r") as file:
                result = file.read()

            expected = """# JSON Comparison


## application

### version
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

        with tempfile.TemporaryDirectory() as temp_dir:
            convert_dict_to_markdown(diff_dict, temp_dir, depth=1)

            output_path = os.path.join(temp_dir, "json_comparison.md")

            with open(output_path, "r") as file:
                result = file.read()

            expected = """# JSON Comparison


## application

### environment
- file1_value: production
- file2_value: staging

## server

### port
- file1_value: 443
- file2_value: 8443

## allowed_regions
- file1_value:
  - us-east-1
  - us-west-2
  - us-west-1
- file2_value:
  - us-east-1
  - us-west-2"""

        self.assertEqual(result, expected)
    
