write_file = open("/root/py/write_file.txt", "w")
write_file.write("This is the first line of the file\n")
write_file.writelines(["and the second\n", "and the third!\n"])
write_file.close()

