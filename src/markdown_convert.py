import os


def convert_dict_to_markdown(diff_dict, missing_keys, destination, depth):
    
    heading = "#" * depth
    file_name = "json_comparison.md"
    full_path = os.path.join(destination, file_name)
    
    set_md_heading(heading, full_path)
    if missing_keys != {}:
        with open(full_path, "a") as file:
            file.write(f"\n## Missing Keys")
        write_missing_keys(missing_keys, full_path, depth=3)
    if diff_dict != {}:
        with open(full_path, "a") as file:
            file.write(f"\n\n## Value Differences")
        write_dict_to_markdown(diff_dict, full_path, depth=3)

def set_md_heading(heading, full_path):
    
    with open(full_path, "a") as file:
        file.write(f"{heading} JSON Comparison\n")

    return

def write_missing_keys(missing_keys, full_path, depth):
    
    for key, value in missing_keys.items():
        heading = depth * "#"
        with open(full_path, "a") as file:
            file.write(f"\n\n{heading} Missing from {key}")
        for i in value:
            with open(full_path, "a") as file:
                file.write(f"\n- {i}")


def write_dict_to_markdown(value_dict, full_path, depth):
        
    for key, value in value_dict.items():
        if isinstance(value, dict):
            adjusted_heading = depth * "#"
            with open(full_path, "a") as file:
                file.write(f"\n\n{adjusted_heading} {key}")
            write_dict_to_markdown(value, full_path, depth=depth+1)
        elif isinstance(value, list):
            data_tuple = (key, value)
            write_dict_to_markdown_list(data_tuple, full_path, depth=depth+1)
        else:
            adjusted_heading = depth * "#"
            with open(full_path, "a") as file:
                file.write(f"\n- {key}: {value}")

def write_dict_to_markdown_list(data_tuple: tuple[str, list[str]], full_path, depth):
    
    key, list_value = data_tuple
    adjusted_heading = depth * "#"
   
    with open(full_path, "a") as file:
        file.write(f"\n- {key}:")
    for i in list_value:
        with open(full_path, "a") as file:
            file.write(f"\n  - {i}")
    return
        
