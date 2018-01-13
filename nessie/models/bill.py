class Bill():

    def __init__(self, _json):
        print(_json)
        self.id = _json["_id"]
        self.status = _json["status"]
        self.payee = _json["payee"]
        self.nickname = _json["nickname"]
        self.creation_date = _json["creation_date"]
        self.payment_date = _json["payment_date"]
        self.recurring_date = _json["recurring_date"]
        self.account_id = _json["account_id"]

    def to_dict(self):
        return vars(self)

# """
# {
#   "_id": "string",
#   "status": "pending",
#   "payee": "string",
#   "nickname": "string",
#   "creation_date": "2017-12-11",
#   "payment_date": "2017-12-11",
#   "recurring_date": 0,
#   "upcoming_payment_date": "2017-12-11",
#   "account_id": "string"
# }
# """