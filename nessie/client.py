import os
from nessie.customerRequests import CustomerRequests
from nessie.accountRequests import AccountRequests

from nessie.billRequests import BillRequest

class Client():
    def __init__(self, nessie_api_key=None):
        # if no key is set then fetch from environment
        if nessie_api_key is None:
            self.key = os.environ['NESSIE_API_KEY']
        else:
            self.key = nessie_api_key
            
        self.account = AccountRequests(self.key)
        self.bill = BillRequest(self.key)
        