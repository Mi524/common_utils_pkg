import sys
sys.path.append("..")

from data_handle_func import *
import unittest 


class TestCase(unittest.TestCase):

	standard_dict = { 
		'PD1805F_EX':'NEX',
		'PD1945F/FF/CF/DF/EF/FF':'S1',
		'PD1945BF/DF/FF_EX':'S1Pro'
	}

	standard_dict = {
		'印尼':'印度尼西亚',
		'马来':'马来西亚'
	}

	replace_dict = {'([a-zA-Z]{1,4}[0-9]{3,5}[a-z]{0,3})_.+':'\g<1>',
					'Dual':'双屏版'}

	def test_check_similarity_strict(self):
		pass
		# print(check_similarity_simple('PD1945F_EX_A_1.8.18', standard_dict, [], {} ))

	def test_replace_by_dict(self):

		test_string = 'PD1945F_EX_A_1.8.18'
		test_string = 'A12(dual)'

		test_string = replace_by_dict(test_string, self.replace_dict)

		print('result:', test_string)

	def test_standardize_by_similarity(self):
		not_standard_str = 'PD1945F_EX_A_1.8.18'
		not_standard_str = '印尼'

		result = standardize_by_similarity(not_standard_str, self.standard_dict, [], {}, mode='simple_lcs')

		print(result)

# def standardize_by_similarity( not_standard_str, standard_dict, special_syn_list,
#                                replace_dict={},  mode ='filter_lcs',ignore_punctuation=True):

if __name__ == "__main__":
	unittest.main()