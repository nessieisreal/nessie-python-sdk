import unittest
import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,path+'/../')

from nessie.dataRequest import DataRequest

class TestDataRequests(unittest.TestCase):
    def test_data_delete_transfers(self):
        pass