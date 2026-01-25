from functions.get_files_info import get_files_info

print("Result for current directory:")
res = get_files_info("calculator", ".")
print(res)

print("Result for 'pkg' directory")
res = get_files_info("calculator", "pkg")
print(res)

print("Result for '/bin' directory:")
res = get_files_info("calculator", "/bin")
print(res)

print("Result for '../' directory:")
res = get_files_info("calculator", "../")
print(res)
