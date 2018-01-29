from models.address import Address


class Merchant:

    def __init__(self, jsonData):
        self.name = jsonData.get('name')
        self.category = jsonData.get('category')
        self.geocode = jsonData.get('geocode')
        address_data = jsonData.get('address')
        if (address_data is not None):
            self.address = Address(address_data.get('street_number'),
                                    address_data.get('street_name'),
                                    address_data.get('city'),
                                    address_data.get('state'),
                                    address_data.get('zip'))
        else:
            self.address = None
        self.merchant_id = jsonData.get('_id')

    def to_dict(self):
        return_dict = {}
        return_dict['name'] = self.name
        return_dict['category'] = self.category
        return_dict['geocode'] = self.geocode
        if (self.address is not None):
            return_dict['address'] = self.address.to_dict()
        return return_dict