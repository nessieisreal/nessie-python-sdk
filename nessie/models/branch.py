class Branch(object):

    def __init__(self, jsonData):
        self._id = jsonData.get('_id')
        self.name = jsonData.get('name')
        self.phone_number = jsonData.get('phone_number')
        self.hours = jsonData.get('hours')
        self.notes = jsonData.get('notes')
        self.address = jsonData.get('address')
        self.geocode = jsonData.get('geocode')

    def to_dict(self):
        return_dict = {}
        return_dict['_id'] = self.id
        return_dict['name'] = self.name
        return_dict['phone_number'] = self.phone_number
        return_dict['address'] = self.address
        return_dict['notes'] = self.notes
        return_dict['hours'] = self.hours
        return_dict['geocode'] = self.geocode
        return return_dict

    def __str__(self):
        return f'Branch Name: {self.name}. Branch ID: {self._id}.'
