import sys
sys.path.append("..")

from os_functions import choose_require_folder, choose_require_folder
import unittest 

class TestCase(unittest.TestCase):


	def test_choose_require_folder(self):
		self.assertEqual(choose_require_folder('..\\'),['tests'])


if __name__ == '__main__':
	unittest.main()






