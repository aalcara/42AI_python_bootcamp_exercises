def text_analyzer(text="", *args):
	"""This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
	if args:
		print("ERROR")
		return
	if text == "":
		text = input(f"What is the text to analyse?\n") 
	len = upper = lower = space = punct = 0
	for char in text:
		len += 1
		if char.isupper():
			upper += 1
		elif char.islower():
			lower += 1
		elif char == ' ':
			space += 1
		elif ('.,!?:;'.find(char) != -1):
			punct += 1
	result = f'''The text contains {len} characters:
- {upper} upper letters
- {lower} lower letters
- {punct} punctuation marks
- {space} spaces'''
	print (result)

