# from sys import argv
# lst = " ".join(argv[1:])
# print(lst[::-1].swapcase())

import sys
args = sys.argv
args.pop(0)
res = ""
for arg in args:
	res += ' ' + arg
res = res[1:]
res = res [::-1].swapcase()
print (res)
