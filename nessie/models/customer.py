from nessie.models.address import Address


class Customer:
    def __init__(self, json_data=None):
        if json_data is None:
            self.first_name = ""
            self.last_name = ""
            self.address = None
            self.customer_id = ""
        else:
            address_data = json_data.get("address")
            self.first_name = json_data.get("first_name")
            self.last_name = json_data.get("last_name")
            self.address = Address(address_data.get("street_number"),
                                   address_data.get("street_name"),
                                   address_data.get("city"),
                                   address_data.get("state"),
                                   address_data.get("zip"))
            self.customer_id = json_data.get("_id")

    def to_dict(self):
        return {
            "_id": self.customer_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address.to_dict()
        }
