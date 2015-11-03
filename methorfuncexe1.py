import hashlib

def md5(file_path):
	"""Return an md5 checksum for a file."""
	read_file = file(file_path)
	the_hash = hashlib.md5()
	for line in read_file.readlines():
		the_hash.update(line)
	return the_hash.hexdigest()

def directory_listing(dir_name):
	"""Return all of the files in a directory."""
	dir_file_list = {}
	dir_root = None
	dir_trim = 0
	for path, dirs, files in os.walk(dir_name):
		if dir_root is None:
			dir_root = path
			dir_trim = len(dir_root)
			print "dir", dir_name,
			print "root is", dir_root
		trimmed_path = path[dir_trim:]
		if trimmed_path.startswith(os.path.sep):
			trimmed_path = trimmed_path[1:]
		for each_file in files:
			file_path = os.path.join(
							trimmed_path,each_file)
			dir_file_list[file_path] = True
	return (dir_file_list, dir_root)

