class Account:

    TYPES = {"Checking", "Credit Card", "Savings"}

    def __init__(self, _id, account_type, nickname, rewards, balance, customer_id, account_number=None):
        self._id = _id
        self.account_type = account_type
        self.nickname = nickname
        self.rewards = rewards
        self.balance = balance
        self.account_number = account_number
        self.customer_id = customer_id
        
    def to_dict(self):
        return vars(self)

    @staticmethod
    def typeIsValid(accountType):
        return accountType in Account.TYPES

    @staticmethod
    def accountNumberIsValid(accountNumber):
        return len(accountNumber) == 16 and accountNumber.isdigit()

    @classmethod
    def fromJson(cls, json):
        obj = cls(json.get("_id"), json.get("type"), json.get("nickname"), 
            json.get("rewards"), json.get("balance"), json.get("customer_id"))
        if "account_number" in json:
            obj.account_number = json.get("account_number")
        return obj
