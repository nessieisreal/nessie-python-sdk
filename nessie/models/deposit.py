class Deposit():

    def __init__(self, _json):
        self.id = _json["_id"]
        self.type = _json["type"]
        if "transaction_date" in _json:
            self.transaction_date = _json["transaction_date"]
        if "status" in _json:
            self.status = _json["status"]
        self.amount = _json["amount"]
        self.payee_id = _json["payee_id"]
        self.medium = _json["medium"]
        if "description" in _json:
            self.description = _json["description"]

    def to_dict(self):
        return vars(self)
