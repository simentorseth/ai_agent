import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    try:
        absolute_path = os.path.abspath(working_directory)
        target_directory = os.path.join(absolute_path, file_path)
        target_directory = os.path.normpath(target_directory)
        target_dir_is_valid = os.path.commonpath(
            [absolute_path, target_directory]) == absolute_path
        target_dir_is_file = os.path.isfile(target_directory)

        if not target_dir_is_valid:
            error_string = f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            return error_string

        if not target_dir_is_file:
            error_string = f'Error: File not found or is not a regular file: "{file_path}"'
            return error_string

        if not target_directory.endswith(".py"):
            error_string = f'Error: "{file_path}" is not a Python file'
            return error_string

        command = ["python3", target_directory]
        if args:
            command.extend(args)

        process = subprocess.run(
            command, capture_output=True, text=True, timeout=30)

        output = ""
        if process.returncode:
            output += f"Process exited with code {process.returncode}\n"
        elif process.stdout:
            output += f"STDOUT: {process.stdout}\n"
        elif process.stderr:
            output += f"STDERR: {process.stderr}\n"
        else:
            output += f"No output produced\n"

        return output

    except Exception as e:
        error_string = f'Error: {e} occurred while trying to execute python file\n'
        return error_string
