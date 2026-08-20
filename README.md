# JSON Comparison Tool
This tool is meant to take two JSON files in the content directory and compare them. If differences are found the tool iterates over the two files and identifies missing keys and value differences.

## Features
- Compares two JSON documents and identifies the differences between them
- Provides a structured markdown report with the findings with headings and subheadings
- Provides a count for missing keys between the two files and the value differences in pairs
- Provides the absolute path location for the markdown comparison file

## How It Works
- User places two JSON files to the content directory then provides them as arguments when running ./main.sh
- The tool verifies that both arguments are provided and that they are both JSON file types
- The comparison generator is started and returns two dictionaries. One for missing keys and one for value differences
- The output directory is cleared of any files that currently reside in the directory to prepare for the new markdown report
- If either dictionary contains differences the markdown generation starts but if the files are the same it prints a message to identify the similarity and the tool closes
- The markdown report generation uses markdown headings to separate out the differences. For example: # JSON Comparison, ## Missing Keys, ### Missing from file1, - feature.enabled_beta_dashboard
- After the markdown report has been generated into the output directory the missing key count and value differences are calculated
- Once the missing key count and value differences have been calculated the tool prints a message indicating that differences were found, how many it found and provides the absolute path to the markdown report

## Project Structure
JSON-Comparison/
├── content/
│   ├── config_a.json
│   └── config_b.json
├── main.sh
├── output/
│   └── json_comparison.md
├── README.md
├── src/
│   ├── difference_count.py
│   ├── json_compare.py
│   ├── main.py
│   ├── markdown_convert.py
│   ├── test_differences.py
│   ├── test_json_compare.py
│   └── test_markdown_convert.py
└── test.sh

## Usage
1. Clone the repository and navigate to the project directory
2. Place the two JSON files you want to compare in the content/ directory
3. Run the comparison tool by passing both filenames as arguments

./main.sh content/config_a.json content/config_b.json

If differences are found, the tool will:
1. Display the number of missing keys
2. Display the number of value differences
3. Generate a Markdown comparison report
4. Print the absolute path to the generated report

The generated report can be found in:
output/json_comparison.md

If not differences are found, the tool will indicate that the files are the same and exit without generating a comparison report

## Example Output
Starting JSON Comparison Tool
Differences found
Comparison complete
Missing keys: 4
Value Differences: 10
Comparison report can be found here: /home/wesleywright/BootDev/JSON-Comparison/output/json_comparison.md

## Running Tests
The project includes unit tests for the JSON comparison, Markdown generation and difference counting functionality

To run the full test suite from the project root:
./test.sh

The tests use Python's built in unittest framework and do not require any additional testing dependencies

## What I Learned
Building this project helped me strengthen my understanding of several Python and software development concepts

- Breaking down complex problems: I learned to separate the comparison process into smaller responsibilities, including finding missing keys, comparing values, counting differences and generating the final report. This made the code easier to understand, test and debug
- Working with recursion: Comparing nested JSON objects gave me experience using recursive functions to walk the dictionaries and return the results through multiple levels of nested data
- Designing data flow between functions: I gained a better understanding of how to structure function return values so that the output from one part of the application can be used by another, such as passing comparison results to the Markdown report generator
- Separating application responsibilities: I organized the comparison logic, Markdown generation, difference counting and CLI orchestration into separate modules rather than placing all the functionality in a single file
- File and path management: I gained additional experience working with files and directories in Python. This includes validating files, reading JSON data, generating output files, managing output directories and working with absolute and relative paths
- Unit Testing: Writing tests throughout development helped me identify problems earlier and gave me experience testing both comparison logic and file generation. I also learned how temporary directories can be used to test file operations without affecting the project's actual output
- Debugging recursive programs: Troubleshooting the comparison logic taught me to trace data through recursive function calls and examine intermediate values instead of focusing only on the final output

Overall, this project gave me experience taking an idea from an initial requirement through implementation, testing, debugging and creating a usable command line interface 
