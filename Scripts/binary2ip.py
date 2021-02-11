#!/usr/bin/python3

bin_num = '10000001.11111111.00000001.11111111'
ip_address = ''
bin_list = bin_num.split('.')

for item in bin_list:
	num_key_start = 128
	cur_num = 0
	for num in item:
		if int(num) == 1:
			dec_num = num_key_start
			cur_num = cur_num + dec_num
		num_key_start = num_key_start // 2

	ip_address = ip_address + str(cur_num) + '.'
ip_address = ip_address[:-1]
print(ip_address)

