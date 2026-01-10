# What does the agent do?

The CLI tool does the following:

1. Accepts a task as an input.
2. Picks a function from a predefined set of functions to work on the task. The predefined functions are:
   - Scan the files in the directory
   - Read a file's contents
   - Overwrite a file's contents
   - Execute the Python interpreter on a file
3. Repeats step 2 until the task is complete (or fails).

