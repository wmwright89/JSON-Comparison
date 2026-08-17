import os
from json_compare import verifyJSON, start_compare

def main():
    json_1 = "content/config_a.json"
    json_2 = "content/config_b.json"
    
    abs_path_1 = os.path.abspath(json_1)
    abs_path_2 = os.path.abspath(json_2)
    print("Starting Comparison")

    verifyJSON(json_1, json_2)
    start_compare(json_1, json_2)


if __name__ == "__main__":
    main()
    
