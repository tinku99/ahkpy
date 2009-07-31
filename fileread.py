import os
def fileread(file):
#    open(file, 'r') as f:
    read_data = file.read()
    return read_data

print fileread("test.py")
