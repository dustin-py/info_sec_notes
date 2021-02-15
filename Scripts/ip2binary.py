#!/usr/bin/python3
import sys


choi = input(
"""
-========================-
|Choose conversion type: |
|a. ip2binary 	         |
|b. binary2ip 	         |
-========================-
Choice: 
""")


def check_for_binary_ip():
	if len(sys.argv) > 1:
		bin_ip = sys.argv[1]
	else:
		print("="*50)
		bin_ip = input('Please type the binary IP address you wish to convert: ')
		print("="*50)
	binary_octet_list = bin_ip.split('.')
	return binary_octet_list
	

def check_for_ip():
	if len(sys.argv) > 1:
		ip = sys.argv[1]
	else:
		print("="*50)
		ip = input('Please type the IP address you wish to convert: ')
		print("="*50)
	ip_segment_list = ip.split('.')
	return ip_segment_list


def check_bits(bits):
	if len(bits) < 8:
			zeros_total = 8 - len(bits)
			bits = bits + '0' * zeros_total
	return bits


def convert_ip2binary(ip_segment_list):
	bin_nums = []
	for num in ip_segment_list:
		position_num = 128
		bits = ''
		tmp_num = int(num)
		while tmp_num != 0 and position_num != 0:
			bits = bits + str(tmp_num // position_num)
			tmp_num = tmp_num % position_num
			position_num = position_num // 2
		bits = check_bits(bits)
		bin_nums.append(bits)
	return bin_nums

def convert_binary2ip(bin_octet_list):
	ip_address = ''
	for item in bin_octet_list:
		num_key_start = 128
		cur_num = 0
		for num in item:
			if int(num) == 1:
				dec_num = num_key_start
				cur_num = cur_num + dec_num
			num_key_start = num_key_start // 2

		ip_address = ip_address + str(cur_num) + '.'
	ip_address = ip_address[:-1]
	return ip_address


if __name__ == "__main__":
	if choi == 'a':
		ip_segment_list = check_for_ip()
		binary_ip = convert_ip2binary(ip_segment_list)
		print("="*69)
		print("  Your converted IP address is: {}".format('.'.join(binary_ip)))
		print("="*69)
	elif choi == 'b':
		bin_octet_list = check_for_binary_ip()
		dec_ip = convert_binary2ip(bin_octet_list)
		print("="*47)
		print("  Your converted binary ip is: {}".format(dec_ip))
		print("="*47)