import os
from nessie.customerRequests import CustomerRequests
from nessie.accountRequests import AccountRequests

from .dataRequest import DataRequest

from nessie.billRequests import BillRequest
from nessie.depositRequests import DepositRequest

class Client():
    def __init__(self, nessie_api_key=None):
        # if no key is set then fetch from environment
        if nessie_api_key is None:
            self.key = os.environ['NESSIE_API_KEY']
        else:
            self.key = nessie_api_key

        self.account = AccountRequests(self.key)
        self.bill = BillRequest(self.key)
        self.data = DataRequest(self.key)
        self.deposit = DepositRequest(self.key)
        self.customer = CustomerRequests(self.key)
