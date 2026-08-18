import os


def convert_dict_to_markdown(diff_dict, destination, depth):
    
    heading = "#" * depth
    file_name = "json_comparison.md"
    full_path = os.path.join(destination, file_name)
    
    if depth == 1:
        set_md_heading(heading, full_path)

    for key, value in diff_dict.items():
        if isinstance(value, dict):
            adjusted_heading = (depth + 1) * "#"
            with open(full_path, "a") as file:
                file.write(f"\n\n{adjusted_heading} {key}")
            convert_dict_to_markdown(value, destination, depth=depth+1)
        else: 
            with open(full_path, "a") as file:
                file.write(f"\n- {key}: {value}")


def set_md_heading(heading, full_path):
    
    with open(full_path, "a") as file:
        file.write(f"{heading} JSON Comparison")

    return
                        
