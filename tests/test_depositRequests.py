import unittest
import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,path+'/../')

from nessie.accountRequests import AccountRequests
from nessie.billRequests import BillRequest
from nessie.dataRequests import DataRequest
from nessie.client import Client
from nessie.models.address import Address

class TestDepositRequests(unittest.TestCase):
    # create some dummy bills
    def setUp(self):
        # implicitly get NESSIE_API_KEY from env
        self.client = Client()
        customer_factory = self.client.customer
        self.customer_id = customer_factory.create_customer("Test", "Customer", Address("123", "Test Street", "TestCity", "VA", "12345")).customer_id
        account_factory = self.client.account
        self.account_id = account_factory.create_customer_account(self.customer_id, "Savings", "Test Account", 0, 100)._id
        self.deposit_factory = self.client.deposit


    def tearDown(self):
        None

    def test_create_deposit_all_fields(self):
        print("test_create_deposit_all_fields")
        result = self.deposit_factory.create_deposit(self.account_id, 'balance', 73, "2018-02-01", 'pending', "test").to_dict()
        self.assertEqual(result['transaction_date'], '2018-02-01')
        self.assertEqual(result['payee_id'], self.account_id)
        self.assertEqual(result['amount'], 73)
        self.deposit_id = result['id']

    def test_create_deposit_min_fields(self):
        print("test_create_deposit_min_fields")
        result = self.deposit_factory.create_deposit(self.account_id, 'balance', 53).to_dict()
        self.assertEqual(result['payee_id'], self.account_id)
        self.assertEqual(result['amount'], 53)
        self.deposit_id2 = result['id']

    def test_create_deposit_optional_fields(self):
        print("test_create_deposit_optional_fields")
        result = self.deposit_factory.create_deposit(self.account_id, 'balance', 6, description='testing').to_dict()
        self.assertEqual(result['description'], 'testing')
        self.assertEqual(result['payee_id'], self.account_id)
        self.assertEqual(result['amount'], 6)

    def test_create_deposit_bad_account(self):
        print("test_create_deposit_bad_account")
        result = self.deposit_factory.create_deposit("59fb2c49b390353c9512sv45", 'balance', 6)

    def test_get_deposit(self):
        print("test_get_deposit")
        result = self.deposit_factory.get_deposit(self.deposit_id).to_dict()

    def test_get_deposit_fail(self):
        print("test_get_deposit_fail")
        result = self.deposit_factory.get_deposit(self.deposit_id).to_dict()

    def test_get_account_deposits(self):
        print("test_get_account_deposits")
        result = self.deposit_factory.get_account_deposits(self.account_id).to_dict()

    def test_get_account_deposits_fail(self):
        print("test_get_account_deposits_fail")
        result = self.deposit_factory.get_account_deposits("59fb2c49b390353c9512sv45").to_dict()

    def test_update_deposit_all_fields(self):
        print("test_update_deposit_all_fields")
        result = self.deposit_factory.update_deposit(self.deposit_id, 'balance', 6, "test Updated").to_dict()
        self.assertEqual(result['amount'], 6)
        self.assertEqual(result['description'], "test Updated")

    def test_update_deposit_fail(self):
        print("test_update_deposit_fail")
        result = self.deposit_factory.update_deposit("", 'balance', 77).to_dict()

    def test_delete_deposit(self):
        print("test_delete_deposit")
        result = self.deposit_factory.delete_deposit(self.deposit_id)

    def test_delete_deposit_fail(self):
        print("test_delete_deposit_fail")
        result = self.deposit_factory.delete_deposit("")


    # try fetching a bill that doesn't exist
    def test_get_nonreal_bill_fail(self):
        print("test_get_nonreal_bill_fail")
        bill_factory = self.client.bill

        result = bill_factory.get_bill("fake")
        expected_result = {'code':404, 'message':'Invalid ID'}
        # {'code':401, 'message':'unauthorized'}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
