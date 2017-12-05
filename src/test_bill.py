import bill
import unittest

class TestBill(unittest.TestCase):

    def test_get_bill_succeed(self):
        bill_factory = bill.Bill("24bb950537c1164a2fbb1bf2a37c3267")
        result = bill_factory.get_bill("5a261c3883a71c405074fcbd")
        test_result = {'_id': '5a261c3883a71c405074fcbd', 'status': 'pending', 'payee': 'string', 'nickname': 'string', 'payment_date': '2017-12-05', 'recurring_date': 1, 'payment_amount': 23, 'creation_date': '2017-12-05', 'account_id': '5a261a0483a71c405074fcbc'}
        self.assertEqual(result, test_result)

    # try fetching a bill that doesn't exist
    def test_get_bill_fail(self):
        bill_factory = bill.Bill("24bb950537c11642fbb1bf2a37c3267")
        result = bill_factory.get_bill("fake")
        print(result)
        