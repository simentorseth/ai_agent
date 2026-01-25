import os

def get_files_info(working_dir, dir="."):
    absolute_path = os.path.abspath(working_dir)
    target_directory = os.path.join(absolute_path, dir)
    target_directory = os.path.normpath(target_directory)
    target_dir_is_valid = os.path.commonpath([absolute_path, target_directory]) == absolute_path
    target_dir_is_dir = os.path.isdir(target_directory)
    
    if not target_dir_is_dir:
        raise ValueError(f'Error: "{target_directory}" is not a directory')
    
    if not target_dir_is_valid:
        raise ValueError(f'Error: Cannot list "{target_directory}" as it is outside the permitted working directory')
    
    dir_items = os.listdir(target_directory)
    output = ""
    for item in dir_items:
        file_path = target_directory + "/" + item
        file_name = item
        file_size = os.path.getsize(file_path)
        is_dir = os.path.isdir(file_path)
        s = f"- {file_name}: file_size={file_size} bytes, is_dir={is_dir}\n"
        output += s
    
    return output


files = get_files_info("calculator",".")
print(files)
