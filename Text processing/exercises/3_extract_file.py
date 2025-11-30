text = input()

name_part, extension = text.rsplit(".", 1)
file_name = name_part.rsplit("\\", 1)[-1]
print(f"File name: {file_name}")
print(f"Extension: {extension}")