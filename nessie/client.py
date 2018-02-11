import os
from nessie.customerRequest import CustomerRequest
from nessie.accountRequest import AccountRequest

from .dataRequest import DataRequest

from nessie.billRequest import BillRequest
from nessie.depositRequest import DepositRequest

class Client():
    def __init__(self, nessie_api_key=None):
        # if no key is set then fetch from environment
        if nessie_api_key is None:
            self.key = os.environ['NESSIE_API_KEY']
        else:
            self.key = nessie_api_key

        self.account = AccountRequest(self.key)
        self.bill = BillRequest(self.key)
        self.data = DataRequest(self.key)
        self.deposit = DepositRequest(self.key)
        self.customer = CustomerRequest(self.key)
