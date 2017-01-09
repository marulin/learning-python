__author__ = 'rollin'

import unittest

from kazoo.client import KazooClient

class TestZK(unittest.TestCase):

	def setUp(self):
		print("begin")

	def test_search_valid(self):
		# curl http and get response
		print("test zk valid")
		zk = KazooClient(hosts='localhost:2181')
		zk.start()
		data, stat = zk.get("/autoconfig/config/x")
		print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))
		zk.set("/autoconfig/config/x", b"some data")
		print("test zk valid end")
		zk.stop()

	def test_search_response(self):
		#
		print("test zk response")

	def tearDown(self):
		print("end")

		if __name__ == '__main__':
			unittest.main()

