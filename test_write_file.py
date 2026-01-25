from functions.write_file import write_file


print("Result for 'lorem.txt':")
res = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(res)

print("Result for 'pkg/morelorem.txt':")
res = write_file("calculator", "pkg/morelorem.txt",
                 "lorem ipsum dolor sit amet")
print(res)

print("Result for '/tmp/temp.text':")
res = write_file("calculator", "/tmp/temp.text", "this should not be allowed")
print(res)
