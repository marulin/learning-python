__author__ = 'rollin'

import unittest

class TestSuggest(unittest.TestCase):

	def setUp(self):
		print("begin")

	def test_valid(self):
		# curl http and get response
		print("test valid")

	def test_response(self):
		#
		print("test response")

	def tearDown(self):
		print("end")

		if __name__ == '__main__':
		    unittest.main()