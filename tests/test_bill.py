import unittest
import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,path+'/../')

from nessie.models.bill import Bill

class TestBill(unittest.TestCase):

    def test_bill_creation(self):
        
        temp = {
            "_id": "string",
            "status": "pending",
            "payee": "string",
            "nickname": "string",
            "creation_date": "2017-12-11",
            "payment_date": "2017-12-11",
            "recurring_date": 0,
            "upcoming_payment_date": "2017-12-11",
            "account_id": "string"
        }
        b = Bill(temp)
        self.assertEqual(b.to_dict()["payee"],temp["payee"])

# acc 5a2619ed83a71c405074fcbb