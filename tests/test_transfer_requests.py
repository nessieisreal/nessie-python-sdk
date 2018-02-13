import unittest
import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,path+'/../')

from nessie.accountRequests import AccountRequests
from nessie.billRequests import BillRequest
from nessie.dataRequests import DataRequests
from nessie.client import Client
from nessie.utils.exceptions import NessieApiError


# def test_create_bill(self):
#     bill_factory = billRequests.BillRequest("wkey")



class TestBillRequests():
    # create some dummy bills
    def setUp(self):
        # implicitly get NESSIE_API_KEY from env
        self.client = Client()
        
        bill_factory = self.client.bill
        bill = bill_factory.create_bill(account_id,
            status='pending',
            payee='bobby',
            nickname='bob',
            payment_date='2018-01-10',
            recurring_date=1,
            payment_amount=10
        )

    def tearDown(self):
        data_deletor = self.client.data
        response = data_deletor.delete_data('Bills')
        d = DataRequests('7e9b72fdb7b286fcd0aae87deb0e09a2')
        d.delete_data('Bills')
        
        

    def test_get_bill_succeed(self):
        print("test_get_bill_succeed")
        bill_factory = self.client.bill
        result = bill_factory.get_account_bills(account_id)
        print(result)
        # result = bill_factory.get_bill("5a261c3883a71c405074fcbd")
        # expected_result = {'bill_id': '5a261c3883a71c405074fcbd', 'status': 'pending', 'payee': 'string', 'nickname': 'string', 'payment_date': '2017-12-05', 'recurring_date': 1, 'payment_amount': 23, 'creation_date': '2017-12-05', 'account_id': '5a261a0483a71c405074fcbc'}
        self.assertEqual(result[0]['payment_date'], '2018-01-10')
        data_deletor = DataRequests(wkey)

    # try fetching a bill that doesn't exist
    def test_get_nonreal_bill_fail(self):
        print("test_get_nonreal_bill_fail")
        bill_factory = self.client.bill
        
        expected_status_code = 404
        # expected_message = 'Invalid ID'
        result = {}
        try:
            try_result = bill_factory.get_bill("fake")
        except NessieApiError as e:
            result = e
            
        self.assertEqual(result.code,expected_status_code)
        
        