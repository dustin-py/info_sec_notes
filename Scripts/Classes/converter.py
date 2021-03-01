"""Module for conversion functions"""
from Classes import utils


class Converter:
    def __init__(self, item_to_convert):
        self.item_to_convert = item_to_convert

    def convert_ip2binary(self):
        bin_nums = []
        for num in self.item_to_convert:
            position_num = 128
            bits = ''
            tmp_num = int(num)
            while tmp_num != 0 and position_num != 0:
                bits = bits + str(tmp_num // position_num)
                tmp_num = tmp_num % position_num
                position_num = position_num // 2
            bits = utils.check_bits(bits)
            bin_nums.append(bits)
        return bin_nums

    def convert_binary2ip(self):
        ip_address = ''
        for item in self.item_to_convert:
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