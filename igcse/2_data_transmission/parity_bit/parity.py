def parity_bit(parity, data):

	even = False
	count_1s = 0
	for index in range(0, len(data)):
		if data[index] == '1':
			count_1s += 1
	
	if count_1s % 2 == 0:
		even = True
	
	if parity == 'EVEN' and even or parity == 'ODD' and not even:
		return data + '0'
	else:
		return data + '1'


def valid_parity(parity):

	if parity == 'ODD' or parity == 'EVEN':
		return True
	return False


def valid_data(data):

	valid = False
	if len(data) == 7:
		for index in range(7):
			if data[index] != '1' or data[index] != '0':
				valid = False
		valid = True
	return valid

