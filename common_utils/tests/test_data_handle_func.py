import sys
sys.path.append("..")

from data_handle_func import *
import unittest 


class TestCase(unittest.TestCase):

	# standard_dict = {
	# 	'印尼':'印度尼西亚',
	# 	'马来':'马来西亚'
	# }

	# def test_check_similarity_strict(self):

	# 	standard_dict = { 
	# 						'Y15(4+64G)':'Y15',
	# 						'Y15':'Y15',
	# 						'PD1818GF_EX':'Y91',
	# 						'PD1818F_EX':'Y95',
	# 						'PD1945BF/DF/FF_EX':'S1Pro'
	# 					}

	# 	print(check_similarity_strict('Y15', standard_dict, [], {} ))

	# def test_replace_by_dict(self):

	# 	test_string = 'PD1945F_EX_A_1.8.18'
	# 	test_string = 'A12(dual)'

	# 	test_string = replace_by_dict(test_string, self.replace_dict)

	# 	# print('result:', test_string)

	def test_standardize_by_similarity(self):
		standard_dict = { 
					'V20':'V20',
					'V20(2021)':'V20(2021)'
				}

		standard_dict = { 
					'Y51':'Y51',
					'y51L':'Y51L',
					'Y51(PD2044)':'Y51(PD2044)'
				}

		not_standard_str = 'V20 2021'
		not_standard_str = 'Y51LL'
		not_standard_str = 'Y51LO'
		result = standardize_by_similarity(not_standard_str, standard_dict, [], {}, mode='strict_mode')

		print(result)

	# def test_get_save_name(self):
	# 	config_file_dir = '.\\'
	# 	config_table_name = 'process_config-All sources(Others).xlsx'
	# 	data_file_dir = '.\\raw_data_files'

	# 	min_max_date_rage = '2020-11-20'
	# 	result = get_save_name(config_table_name,config_file_dir, min_max_date_rage)

		# print(result)

# def standardize_by_similarity( not_standard_str, standard_dict, special_syn_list,
#                                replace_dict={},  mode ='filter_lcs',ignore_punctuation=True):

if __name__ == "__main__":
	unittest.main()