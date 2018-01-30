import os

from .accountRequests import AccountRequests
from .atmRequests import ATMRequest
from .billRequests import BillRequest
from .branchRequests import BranchRequest
from .customerRequests import CustomerRequests
from .dataRequests import DataRequests

class Client():
    def __init__(self, nessie_api_key=None):
        # if no key is set then fetch from environment
        if nessie_api_key is None:
            try:
                self.key = os.environ['NESSIE_API_KEY']
            except KeyError as e:
                raise Exception(e,"probably need to `export NESSIE_API_KEY=xxxxxxxxxxx`")
        else:
            self.key = nessie_api_key
        
        self.account = AccountRequests(self.key)
        self.atm = ATMRequest(self.key)
        self.bill = BillRequest(self.key)
        self.branch = BranchRequest(self.key)
        self.data = DataRequests(self.key)
        self.customer = CustomerRequests(self.key)
        
        