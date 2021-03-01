#!/usr/bin/python3
from Classes.converter import Converter
from Classes import utils

choi = input(
"""
-========================-
|Choose conversion type: |
|a. ip2binary 	         |
|b. binary2ip 	         |
-========================-
Choice: 
""")

if __name__ == "__main__":
	if choi == 'a':
		ip_segment_list = utils.check_for_ip()
		binary_ip = Converter(ip_segment_list).convert_ip2binary()
		print("="*69)
		print("  Your converted IP address is: {}".format('.'.join(binary_ip)))
		print("="*69)
	elif choi == 'b':
		bin_octet_list = utils.check_for_binary_ip()
		dec_ip = Converter(bin_octet_list).convert_binary2ip()
		print("="*47)
		print("  Your converted binary ip is: {}".format(dec_ip))
		print("="*47)