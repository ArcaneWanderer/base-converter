from math import modf, log10
import unittest

def convert_from_base10_whole(value, radix):
	converted = []
	new_val = ''
	while value > 0:
		if value < radix:
			new_val = str(value)
		else:
			if radix >= 10:
				if value % radix >= 10:
					new_val = get_hex_representation(int(value % radix))
				else:
					new_val = str(int(value % radix))
			else:
				new_val = str(int(value % radix))
		converted.append(new_val)
		value /= radix
	return ''.join(converted)[::-1]

def convert_from_base10_frac(value, radix):
	converted = []
	while modf(value)[0] != 0.0:
		if radix > 10:
			if value % radix >= 10:
				new_val = get_hex_representation(int(modf(value * radix)[1]))
			else:
				new_val = str(int(modf(value * radix)[1]))
		else:
			new_val = str(int(modf(value * radix)[1]))
		converted.append(new_val)
		value = modf(value)[0] * radix
	return ''.join(converted)

def convert_from_base10(value, radix):
	converted = []
	if not isinstance(value, float):
		value = float(value)
	x = modf(value)
	whole, frac = x[1], x[0]
	return convert_from_base10_whole(whole, radix) + '.' + convert_from_base10_frac(frac, radix)

class TestConvertToBase10(unittest.TestCase):

	def test_convert_from_base_10_whole_1(self):
		self.assertEqual(convert_from_base10_whole(4, 2), '100')

	def test_convert_from_base_10_whole_2(self):
		self.assertEqual(convert_from_base10_whole(5, 2), '101')

	def test_convert_from_base_10_whole_3(self):
		self.assertEqual(convert_from_base10_whole(7, 2), '111')

def convert_to_base10_whole(value, radix):
	exp = 0
	converted = 0
	for i in reversed(value):
		if not is_number(i):
			i = get_dec_representation(i)
		new_val = int(i) * (radix ** exp)
		converted += new_val
		exp += 1
	return str(converted)

def convert_to_base10_frac(value, radix):
	exp = -1
	converted = 0
	for i in reversed(value):
		if not is_number(i):
			i = get_dec_representation(i)
		new_val = int(i) * (radix ** exp)
		converted += new_val
		exp += -1
	converted = (int) (converted * (10 ** (len(str(converted))-2)))
	return str(converted)

def convert_to_base10(value, radix):
	converted = []
	if '.' in value:
		x = value.split('.')
		whole, frac = x[0], x[1]
		return convert_to_base10_whole(whole, radix) + '.' + convert_to_base10_frac(frac, radix)
	else:
		return convert_to_base10_whole(value, radix)

def convert_base(value, from_radix, to_radix):
	if (from_radix == 10):
		return convert_from_base10(value, to_radix)
	elif (to_radix == 10):
	 return convert_to_base10(value, from_radix)
	else:
		return convert_from_base10(convert_to_base10(value, from_radix), to_radix)

def get_hex_representation(value):
	return {
		10: 'A',
		11: 'B',
		12: 'C',
		13: 'D',
		14: 'E',
		15: 'F',
	}.get(value, 'Error')

def get_dec_representation(value):
	return {
		'A': 10,
		'B': 11,
		'C': 12,
		'D': 13,
		'E': 14,
		'F': 15,
	}.get(value, -1)

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#print(convert_from_base10(27.25, 16))
#print(convert_to_base10('A4.8', 16))
#print(convert_base('A4.8', 16, 2))
#unittest.main()
to_convert = raw_input("Enter in format: \n<number to convert> <current base> <target base> \n")
to_convert = to_convert.split()
print(convert_base(to_convert[0], int(to_convert[1]), int(to_convert[2])))