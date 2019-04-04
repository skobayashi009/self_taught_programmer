name = input("What is your name: ")

with open("answer.txt", "w") as f:
	f.write(name)