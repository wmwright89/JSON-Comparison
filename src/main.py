import os
from json_compare import verifyJSON, start_compare
from markdown_convert import convert_dict_to_markdown
from difference_count import difference_count_generator
import shutil

def main():
    json_1 = "content/config_a.json"
    json_2 = "content/config_b.json"
    
    print("Starting JSON Comparison Tool")

    verifyJSON(json_1, json_2)
    
    diff_dict, missing_keys = start_compare(json_1, json_2)
    
    destination = "output"
    #Clear previous output before generating a new report
    if not os.path.exists(destination):
        os.mkdir(f"./{destination}")
    else:
        for item in os.listdir(destination):
            full_path = os.path.join(destination, item)
            if os.path.isfile(full_path):
                os.remove(full_path)
            else:
                shutil.rmtree(full_path)

    if diff_dict != {} or missing_keys != {}:
        full_path = convert_dict_to_markdown(diff_dict, missing_keys, destination, depth=1)
        absolute_path = os.path.abspath(full_path)
        key_count, value_count = difference_count_generator(diff_dict, missing_keys)
        print(f"Differences found\nComparison complete\nMissing keys: {key_count}\nValue Differences: {value_count}\nComparison report can be found here: {absolute_path}")
    else:
        print("No differences found\nComparison complete")


if __name__ == "__main__":
    main()
    
