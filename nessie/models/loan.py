class Loan:
    def __init__(self, data_json=None):

        if data_json is None:
            print("Provided json is None. Setting all fields to None.")
            data_json = {}

        self._id = data_json.get('_id', None)
        self.type = data_json.get('type', None)
        self.creation_date = data_json.get('creation_date', None)
        self.status = data_json.get('status', None)
        self.credit_score = data_json.get('credit_score', None)
        self.monthly_payment = data_json.get('monthly_payment', None)
        self.amount = data_json.get('amount', None)
        self.description = data_json.get('description', None)
        self.account_id = data_json.get('account_id', None)
        self.creation_date = data_json.get('creation_date', None)
        self.__check_for_none__()

    def __check_for_none__(self):
        for var in self.__dict__.items():
            if var[1] is None:
                print("WARNING! Key:'{key}' has been set to None".format(key=var[0]))

    def to_dict(self):
        return self.__dict__

