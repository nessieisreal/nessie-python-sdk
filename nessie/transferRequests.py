from .transactionRequests import TransactionRequest
from .models.transfer import Transfer

class TransferRequests(TransactionRequest):
    def __init__(self, api_key):
        super().__init__(api_key, 'transfer',Transfer)