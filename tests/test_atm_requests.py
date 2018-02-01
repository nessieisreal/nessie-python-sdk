import unittest
import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,path+'/../')

from nessie.client import Client

class TestAtmRequests(unittest.TestCase):
    
    def setUp(self):
        # implicitly get NESSIE_API_KEY from env
        self.client = Client()
       
    # no tearDown needed as its 
    # read only functions
    # def tearDown(self):
    #     pass
        
        
    # test_get_atms go intos an infinite loop
    # def test_get_atms(self):
    #     lat = 38.9283
    #     lng = -77.1753
    #     rad = 1
        
    #     observed_atms = self.client.atm.get_atms(lat,lng,rad)
    #     print(observed_atms)
    #     expected_firsttwo_atms = [
    #     {
    #       "_id": "56c66be5a73e492741506f4b",
    #       "name": "McLean 1",
    #       "geocode": {
    #         "lng": -77.17829449999999,
    #         "lat": 38.932887
    #       },
    #       "accessibility": 'true',
    #       "hours": [
    #         "24 hours a day, 7 days a week"
    #       ],
    #       "address": {
    #         "state": "VA",
    #         "zip": "22101",
    #         "city": "McLean",
    #         "street_name": "Chain Bridge Road",
    #         "street_number": "1439"
    #       },
    #       "language_list": [
    #         "English"
    #       ],
    #       "amount_left": 273775
    #     },
    #     {
    #       "_id": "56c66be5a73e492741506f4c",
    #       "name": "McLean 2",
    #       "geocode": {
    #         "lng": -77.17829449999999,
    #         "lat": 38.932887
    #       },
    #       "accessibility": 'false',
    #       "hours": [
    #         "24 hours a day, 7 days a week"
    #       ],
    #       "address": {
    #         "state": "VA",
    #         "zip": "22101",
    #         "city": "McLean",
    #         "street_name": "Chain Bridge Road",
    #         "street_number": "1439"
    #       },
    #       "language_list": [
    #         "Portuguese",
    #         "Korean",
    #         "Spanish",
    #         "Chinese",
    #         "French",
    #         "English"
    #       ],
    #       "amount_left": 444425
    #     }]
        
    #     self.assertEqual(observed_atms,expected_atms)
        
    def test_get_atm(self):
        atm = self.client.atm.get_atm('56c66be5a73e492741506f4b')
        observed_atm = atm.to_dict()
        expected_atm = {
          "_id": "56c66be5a73e492741506f4b",
          "name": "McLean 1",
          "geocode": {
            "lng": -77.17829449999999,
            "lat": 38.932887
          },
          "accessibility": True,
          "hours": [
            "24 hours a day, 7 days a week"
          ],
          "address": {
            "state": "VA",
            "zip": "22101",
            "city": "McLean",
            "street_name": "Chain Bridge Road",
            "street_number": "1439"
          },
          "language_list": [
            "English"
          ],
          "amount_left": 273775
        }
        self.assertEqual(observed_atm, expected_atm)