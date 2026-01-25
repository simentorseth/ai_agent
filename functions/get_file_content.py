import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        absolute_path = os.path.abspath(working_directory)
        target_directory = os.path.join(absolute_path, file_path)
        target_directory = os.path.normpath(target_directory)
        target_dir_is_valid = os.path.commonpath([absolute_path, target_directory]) == absolute_path
        target_dir_is_dir = os.path.isdir(target_directory)

        if not target_dir_is_valid:
            error_string = f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            return error_string

        if not target_dir_is_dir:
            error_string = f'Error: File not found or is not a regular file: "{file_path}"'
            return error_string
            
        with open(target_directory, "r") as file:
            content = file.read(MAX_CHARS)

            if file.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            return content
        
    except Exception as e:
        error_string = f'Error: {e} was raised while getting contents of "{file_path}"'

        
