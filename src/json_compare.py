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
        return_data_1, return_data_2 = key_diff_finder(data_1, data_2)
        diff_dict = value_diff_finder(return_data_1, return_data_2)
        return diff_dict
    else:
        print("Files are the same")
        return True

def key_diff_finder(file1, file2):
    missing_keys_file1 = []
    missing_keys_file2 = []
    return_dict_1 = {}
    return_dict_2 = {}
    
    for key, value in file1.items():
        if key not in file2:
            missing_keys_file1.append(key)
        else:
            file1_value = file1[key]
            file2_value = file2[key]
            if isinstance(file1_value, dict) and isinstance(file2_value, dict):
                child_return_1, child_return_2 = key_diff_finder(file1_value, file2_value)
                return_dict_1[key] = child_return_1
                return_dict_2[key] = child_return_2
            else:
                return_dict_1[key] = file1_value
                return_dict_2[key] = file2_value 

    for key, value in file2.items():
        if key not in file1: 
            missing_keys_file2.append(key)


    return return_dict_1, return_dict_2
        

def value_diff_finder(input1, input2):
    return_dict_1 = {}
    return_dict_2 = {}

    for key, value in input1.items():
        value1 = input1[key]
        value2 = input2[key]

        if isinstance(value1, dict) and isinstance(value2, dict):
             child_return_1 = value_diff_finder(value1, value2)
             return_dict_1[key] = child_return_1
        else:
            if value1 != value2:
                return_dict_1[key] = {
                    "file1_value": value1,
                    "file2_value": value2
                    }

    return return_dict_1
                
            
    
        
