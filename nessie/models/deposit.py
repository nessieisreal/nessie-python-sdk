class Deposit():

    def __init__(self, _json):
        print(_json)
        self.id = _json["_id"]
        self.type = _json["type"]
        self.transaction_date = _json["transaction_date"]
        self.status = _json["status"]
        self.payee_id = _json["payee_id"]
        self.medium = _json["medium"]
        self.description = _json["description"]

    def to_dict(self):
        return vars(self)
