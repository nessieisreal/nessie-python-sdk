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
        
    def test_create_and_customer(self):
        
        customer_json = {
            "first_name":"Adam",
            "last_name":"Smith",
            "address": {
                "street_number": "1",
                "street_name": "Dolly Madison Blvd",
                "city": "Tysons Corner",
                "state": "VA",
                "zip": "12345"
            }
        }
        
        # generated customer from json
        expected_customer = Customer(customer_json)
        
        new_customer = self.client.customer.create_customer(
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
        
        # newly created customer id
        new_customer_id = new_customer.customer_id
        
        # the actual customer created and returned
        actual_customer = self.client.customer.get_customer_by_id(new_customer_id)
        
        # add customer_id on (its impossible for 
        # the expected to know the dynamic id)
        expected_customer.customer_id = actual_customer.customer_id
        
        # print("expected_customer:")
        # print(vars(expected_customer))
        # print("actual_customer:")
        # print(vars(actual_customer))
        # print("id",expected_customer.customer_id)
        self.assertEqual(actual_customer,expected_customer)


    # create customer bill
    # update customer bill
    # get customer bill and verify
    # delete customer bill
    def test_create_update_get_customer(self):
        new_customer = self.client.customer.create_customer(
            first_name = "Bob",
            last_name = "Anderson",
            address = {
                "street_number": "2",
                "street_name": "Dolly Madison Blvd",
                "city": "Tysons Corner",
                "state": "VA",
                "zip": "12345"
            }
        )
        
        # try updating
        
        customer_id = new_customer.customer_id 
        
        self.client.customer.update_customer(
            customer_id,
            {
                    'street_number': '3',
                    "street_name": "Dolly Madison Blvd",
                    "city": "Tysons Corner",
                    "state": "VA",
                    "zip": "12345"
            }
        )
        
        customer = self.client.customer.get_customer_by_id(customer_id)
        expected_address = {
            "street_number": "3",
            "street_name": "Dolly Madison Blvd",
            "city": "Tysons Corner",
            "state": "VA",
            "zip": "12345"
        }
        self.assertEqual(customer.address.to_dict(),expected_address)