
class Transfer():
    def __init__(self, _json):
        self.transfer_id = _json['_id']
        self.type = _json['type']
        self.transaction_date = _json['transaction_date']
        self.status = ['status']
        self.medium = _json['medium']
        self.payer_id = _json['payer_id']
        self.payee_id = _json['payee_id']
        self.description = _json['description']

    def to_dict(self):
        return vars(self)


# """
# "_id": "string",
# "type": "p2p",
# "transaction_date": "2018-02-01",
# "status": "pending",
# "medium": "balance",
# "payer_id": "string",
# "payee_id": "string",
# "description": "string"
# """