from functions.run_python_file import run_python_file


print("Result for 'main.py':")
res = run_python_file("calculator", "main.py")
print(res)

print("\nResult for 'main.py' with args '['3 + 5']':")
res = run_python_file("calculator", "main.py", ["3 + 5"])
print(res)

print("\nResult for 'tests.py':")
res = run_python_file("calculator", "tests.py")
print(res)

print("\nResult for '../main.py':")
res = run_python_file("calculator", "../main.py")
print(res)

print("\nResult for 'nonexistent.py':")
res = run_python_file("calculator", "nonexistent.py")
print(res)

print("\nResult for 'lorem.txt':")
res = run_python_file("calculator", "lorem.txt")
print(res)
