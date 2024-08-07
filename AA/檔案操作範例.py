import os

file_name = 'example.txt'

# 创建一个文件并写入内容
with open(file_name, 'w') as file:
    file.write("Hello, MicroPython!\n")
    file.write("This is a simple file operation example.\n")

print(f"File '{file_name}' created and written.")

# 读取文件内容
with open(file_name, 'r') as file:
    content = file.read()
    print("File content:")
    print(content)

# 追加内容到文件
with open(file_name, 'a') as file:
    file.write("Appending a new line to the file.\n")

print(f"Content appended to '{file_name}'.")

# 删除文件
try:
    os.remove(file_name)
    print(f"File '{file_name}' deleted.")
except OSError as e:
    print(f"Error deleting file '{file_name}': {e}")
