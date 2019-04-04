import os
path = os.path.join("test.txt")



with open(path, "r") as f:
	print(f.read())