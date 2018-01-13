class Address:
    def __init__(self, street_number: str, street_name: str, city: str, state: str, zipcode: str):
        self.street_number = street_number
        self.street_name = street_name
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def to_dict(self):
        return {
            "street_number": self.street_number,
            "street_name": self.street_name,
            "city": self.city,
            "state": self.state,
            "zip": self.zipcode
            }
