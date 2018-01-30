import os
# ordered from highest to lowest scope
from .dataRequests import DataRequests
from .customerRequests import CustomerRequests
from .accountRequests import AccountRequests
from .billRequests import BillRequest

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
        self.bill = BillRequest(self.key)
        self.data = DataRequests(self.key)
        self.customer = CustomerRequests(self.key)
        
        