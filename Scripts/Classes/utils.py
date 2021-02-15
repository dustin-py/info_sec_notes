"""Module for utility functions"""
import sys


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
