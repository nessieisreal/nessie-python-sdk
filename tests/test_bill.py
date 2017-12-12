import unittest
from nessie.models.bill import Bill

class TestBill(unittest.TestCase):

    def test_bill_creation(self):
        b = Bill()
        print("hi")
        print(vars(b))