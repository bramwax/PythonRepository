from parity import *

def main():

	parity = ''
	while not valid_parity(parity):
		parity = input('Enter ODD or EVEN parity: ').upper()
	

	data_in = ''
	while not valid_data(data_in):
		data_in = input("Enter 7-digit binary data: ")

	data_out = parity_bit(parity, data_in)
	print(data_out)

if __name__ == '__main__':
	main()