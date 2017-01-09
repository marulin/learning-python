__author__ = 'rollin'

import unittest

class TestSearch(unittest.TestCase):
	'''search test'''

	def setUp(self):
		print("begin")

	def test_search_valid(self):
		"test search valid"
		# curl http and get response
		print("test search valid")

	def test_search_response(self):
		"teset search response"
		#
		print("test search response")

	def tearDown(self):
		print("end")

		if __name__ == '__main__':
			unittest.main()
