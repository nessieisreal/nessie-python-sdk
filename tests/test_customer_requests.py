import unittest
import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,path+'/../')

from nessie.client import Client
from nessie.customerRequests import CustomerRequests
from nessie.models.customer import Customer

class TestCustomerRequests(unittest.TestCase):
    
    def setUp(self):
        # implicitly get NESSIE_API_KEY from env
        self.client = Client()
        
        self.client.data.delete_data('Customers')
        
        self.client.customer.create_customer(
            first_name = "Adam",
            last_name = "Smith",
            address = {
                "street_number": "1",
                "street_name": "Dolly Madison Blvd",
                "city": "Tysons Corner",
                "state": "VA",
                "zip": "12345"
            }
        )
        
    def tearDown(self):
        self.client.data.delete_data('Customers')
    
    def test_get_customer(self):
        customers = self.client.customer.get_all_customers()
        
        # assert there is one customer
        self.assertEqual(len(customers), 1)
        self.assertEqual(type(customers[0]), Customer)