import os
def run(filename):
    if os.path.isfile(filename):
        execfile(filename)

run("test.py")
