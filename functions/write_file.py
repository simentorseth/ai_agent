import os


def write_file(working_directory, file_path, content):
    try:
        absolute_path = os.path.abspath(working_directory)
        target_directory = os.path.join(absolute_path, file_path)
        target_directory = os.path.normpath(target_directory)
        target_dir_is_valid = os.path.commonpath(
            [absolute_path, target_directory]) == absolute_path
        target_dir_is_dir = os.path.isdir(target_directory)

        if not target_dir_is_valid:
            error_string = f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            return error_string

        if target_dir_is_dir:
            error_string = f'Error: Cannot write to "{file_path}" as it is a directory'
            return error_string

        os.makedirs(target_directory, exist_ok=True)

        with open(target_directory, "w") as file:
            file.write(content)

        success_string = f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        return success_string

    except Exception as e:
        error_string = f"Error: {e} occurred while getting files."
        return error_string
