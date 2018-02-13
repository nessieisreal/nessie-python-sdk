import unittest
import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,path+'/../')

from nessie.client import Client

class TestClient(unittest.TestCase):
    
    def test_client_initialize(self):
        # should implicitly retrieve key from 
        # env.NESSIE_API_KEY
        client = Client()
        
        self.assertIsNotNone(client.key)