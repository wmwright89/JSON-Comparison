def difference_count_generator(diff_dict, missing_keys):
    key_count = 0
    value_count = 0

    if missing_keys != {}:
        for item in missing_keys.values():
                key_count += len(item)

    if diff_dict != {}:
        for key, value in diff_dict.items():
            if isinstance(value, dict):
                value_count += nested_dict_score_generator(value)

    return key_count, value_count


def nested_dict_score_generator(input_dict):
    score = 0
    
    if "file1_value" in input_dict and "file2_value" in input_dict:
        return 1
    
    for value in input_dict.values():
        if isinstance(value, dict):
            score += nested_dict_score_generator(value)

    return score


