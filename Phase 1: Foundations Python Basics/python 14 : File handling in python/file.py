// File handling in Python
# Syntax:
# file = open('filename.txt', 'mode')
file = open("file.txt", "w")

file.write("Hello, this is a file handling example in Python.\n")
file.write("We can write multiple lines to the file.\n")
file.close()

file = open("file.txt", "r")
content = file.read()
print(content)
