import os
import json

def verifyJSON(source_1, source_2) -> bool:

    if not os.path.exists(source_1):
        raise Exception("First file not found")
    if not os.path.exists(source_2):
        raise Exception("Second file not found")

    return True

def start_compare(source_1, source_2):
    with open(source_1, 'r') as file:
        data_1 = json.load(file)
    with open(source_2, 'r') as file:
        data_2 = json.load(file)

    if data_1 != data_2:
        print("Differences found")
        key_diff_finder(data_1, data_2)
       # value_diff_finder(key_diff_finder(data_1, data_2))
    else:
        print("Files are the same")

def key_diff_finder(file1, file2):
    print("Brrrr... starting key diff engine")
    missing_keys_file1 = []
    missing_keys_file2 = []
    return_dict_1 = {}
    return_dict_2 = {}
    
    for key, value in file1.items():
        if key not in file2:
            print(f"file 1 key not found {key}")
            missing_keys_file1.append(key)
        else:
            file1_value = file1[key]
            file2_value = file2[key]
            if isinstance(file1_value, dict) and isinstance(file2_value, dict):
                key_diff_finder(file1_value, file2_value)

    for key, value in file2.items():
        if key not in file1:
            print(f"file 2 key not found {key}")
            missing_keys_file2.append(key)            
        

def value_diff_finder(matching_sets):
    dict_1, dict_2 = matching_sets
    
    for key, value in dict_1.items():
        if value not in dict_2.items():
            print(f"Value: {value} not in dict 2")
    
        
