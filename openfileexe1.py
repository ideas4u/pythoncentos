import os

read_file = file(os.path.join("/root/py/", "times.py"))
file_contents = list(read_file.readlines())
print "Read in", len(file_contents), "lines form times.py"
print "The first line reads:", file_contents[0]
