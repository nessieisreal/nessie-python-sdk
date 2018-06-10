import unittest
import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,path+'/../')

from nessie.accountRequest import AccountRequest
from nessie.billRequest import BillRequest
from nessie.dataRequest import DataRequest
from nessie.utils.exceptions import NessieApiError

# def test_create_bill(self):
#     bill_factory = billRequests.BillRequest("wkey")

wkey = '7e9b72fdb7b286fcd0aae87deb0e09a2'

# customer_id = '5a546ffd6514d52c7774a2ca'
# account_factory = AccountRequests(wkey)
# account_factory.createCustomerAccount(customer_id)

# premade account id
account_id = '5a5471796514d52c7774a2cb'

class TestBillRequests(unittest.TestCase):
    # create some dummy bills
    def setUp(self):
        bill_factory = BillRequest(wkey)
        bill = bill_factory.create_bill(account_id,
            status='pending',
            payee='bobby',
            nickname='bob',
            payment_date='2018-01-10',
            recurring_date=1,
            payment_amount=10
        )

    def tearDown(self):
        data_deletor = DataRequest(wkey)


    # try fetching a bill that doesn't exist
    def test_get_nonreal_bill_fail(self):
        print("test_get_nonreal_bill_fail")
        bill_factory = BillRequest(wkey)
        
        
        expected_status_code = 404
        # expected_message = 'Invalid ID'
        result = {}
        try:
            try_result = bill_factory.get_bill("fake")
        except NessieApiError as e:
            result = e
            
        self.assertEqual(result.code,expected_status_code)
        



        