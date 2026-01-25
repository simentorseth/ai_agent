from functions.get_file_content import get_file_content
from config import MAX_CHARS

print("Result for 'lorem.txt':")
res = get_file_content("calculator", "lorem.txt")
print(len(res))
print(res[MAX_CHARS:len(res)])

print("Result for 'main.py':")
res = get_file_content("calculator", "main.py")
print(res)

print("Result for 'pkg/calculator.py':")
res = get_file_content("calculator", "pkg/calculator.py")
print(res)

print("Result for '/bin/cat':")
res = get_file_content("calculator", "/bin/cat")
print(res)

print("Result for 'pkg/does_not_exist.py':")
res = get_file_content("calculator", "pkg/does_not_exist.py")
print(res)
