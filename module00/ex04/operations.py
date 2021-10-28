from sys import argv

USAGE = f'''Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3'''
MANY_ARG = f'''InputError: too many arguments
'''
ONLY_NUM = f'''InputError: only numbers
'''

if len(argv) < 3:
	print(USAGE)
	exit()
if len(argv) > 3:
	print(MANY_ARG)
	print(USAGE)
	exit()
if not argv[1].isdigit() or not argv[2].isdigit():
	print(ONLY_NUM)
	print(USAGE)
	exit()


sum = int(argv[1]) + int(argv[2])
diff = int(argv[1]) - int(argv[2])
prod = int(argv[1]) * int(argv[2])
if (argv[2] != "0"):
	quot = int(argv[1]) / int(argv[2])
	rema = int(argv[1]) % int(argv[2])
else:
	quot = "ERROR (div by zero)"
	rema = "ERROR (modulo by zero)"


print(f'''Sum:         {sum}
Difference:  {diff}
Product:     {prod}
Quotient:    {quot}
Remainder:   {rema}''')




