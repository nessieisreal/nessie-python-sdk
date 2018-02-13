import unittest
import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,path+'/../')

from nessie.client import Client

class TestBranchRequests(unittest.TestCase):
    
    def setUp(self):
        # implicitly get NESSIE_API_KEY from env
        self.client = Client()
       
    # no tearDown needed as its 
    # read only functions
    # def tearDown(self):
    #     pass
    
    def test_get_branch_succeed(self):
        branch = self.client.branch.get_branch_by_id('56c66be5a73e4927415071a3')
        observed_branch = branch.to_dict()
        expected_branch = {
          "_id": "56c66be5a73e4927415071a3",
          "name": "ARLINGTON",
          "phone_number": "(703) 812-8550",
          "hours": [
            "Sun",
            "Mon 9 AM - 5 PM",
            "Tue 9 AM - 5 PM",
            "Wed 9 AM - 5 PM",
            "Thu 9 AM - 5 PM",
            "Fri 9 AM - 6 PM",
            "Sat 9 AM - 1 PM"
          ],
          "notes": [
            "Safe Deposit Box",
            "Branch Drive-Up",
            "ATM Available",
            "Open on Saturday"
          ],
          "address": {
            "street_number": "4700",
            "state": "VA",
            "street_name": "Lee Highway",
            "zip": "22207",
            "city": "Arlington"
          },
          "geocode": {
            "lng": -77.1211338,
            "lat": 38.8981779
          }
        }
        self.assertEqual(observed_branch, expected_branch)
    
    def test_get_branch_fail(self):
        pass
    
    def test_get_branches_succeed(self):
        pass
    
    def test_get_branches_fail(self):
        pass