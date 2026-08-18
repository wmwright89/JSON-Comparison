import os
from json_compare import verifyJSON, start_compare
from markdown_convert import convert_dict_to_markdown
import shutil

def main():
    json_1 = "content/config_a.json"
    json_2 = "content/config_b.json"
    
    print("Starting JSON Comparison Tool")

    verifyJSON(json_1, json_2)
    diff_dict = {}
    diff_dict, missing_keys = start_compare(json_1, json_2)
    
    destination = "output"
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
        convert_dict_to_markdown(diff_dict, missing_keys, destination, depth=1)


if __name__ == "__main__":
    main()
    
