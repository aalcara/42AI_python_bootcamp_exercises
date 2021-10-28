from sys import argv

if (len(argv) > 2):
	print("ERROR")
elif not argv[1].isdigit():
	print("ERROR")
elif int(argv[1]) == 0:
	print("I'm zero.")
elif int(argv[1]) % 2 == 0:
	print("I'm Odd.")
else:
	print("I'm Even.")