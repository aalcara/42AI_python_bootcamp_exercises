import unittest
# import operations
import sys
from io import StringIO
import os
import contextlib
import subprocess


USAGE = f'''Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3'''
MANY_ARG = f'''InputError: too many arguments

'''
ONLY_NUM = f'''InputError: only numbers

'''

class TestOperations(unittest.TestCase):

	def test_operations_10_3(self):
		temp_stdout = StringIO()
		with contextlib.redirect_stdout(temp_stdout):
			result = subprocess.check_output(['python', 'operations.py', '10', '3']).strip().decode('ascii')
		self.assertEqual(result, f'''Sum:         13
Difference:  7
Product:     30
Quotient:    3.3333333333333335
Remainder:   1''')

	def test_operations_42_10(self):
		temp_stdout = StringIO()
		with contextlib.redirect_stdout(temp_stdout):
			result = subprocess.check_output(['python', 'operations.py', '42', '10']).strip().decode('ascii')
		self.assertEqual(result, f'''Sum:         52
Difference:  32
Product:     420
Quotient:    4.2
Remainder:   2''')

	def test_operations_1_0(self):
		temp_stdout = StringIO()
		with contextlib.redirect_stdout(temp_stdout):
			result = subprocess.check_output(['python', 'operations.py', '1', '0']).strip().decode('ascii')
		self.assertEqual(result, f'''Sum:         1
Difference:  1
Product:     0
Quotient:    ERROR (div by zero)
Remainder:   ERROR (modulo by zero)''')

	def test_operations_no_argv(self):
		temp_stdout = StringIO()
		with contextlib.redirect_stdout(temp_stdout):
			result = subprocess.check_output(['python', 'operations.py']).strip().decode('ascii')
		self.assertEqual(result, USAGE)

	def test_operations_three_argv(self):
		temp_stdout = StringIO()
		with contextlib.redirect_stdout(temp_stdout):
			result = subprocess.check_output(['python', 'operations.py', '12', '10', '5']).strip().decode('ascii')
		self.assertEqual(result, MANY_ARG + USAGE)

	def test_operations_no_nubers(self):
		temp_stdout = StringIO()
		with contextlib.redirect_stdout(temp_stdout):
			result = subprocess.check_output(['python', 'operations.py', '"one"', '"two"']).strip().decode('ascii')
		self.assertEqual(result, ONLY_NUM + USAGE)

	def test_operations_floats_inside_quotes(self):
		temp_stdout = StringIO()
		with contextlib.redirect_stdout(temp_stdout):
			result = subprocess.check_output(['python', 'operations.py', '"512"', '"63.1"']).strip().decode('ascii')
		self.assertEqual(result, ONLY_NUM + USAGE)

if __name__ == '__main__':
	unittest.main()