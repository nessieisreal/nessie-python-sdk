class Branch(object):

    def __init__(self, jsonData):
        self.atmId = jsonData.get('_id')
        self.name = jsonData.get('name')
        self.phone_number = jsonData.get('phone_number')
        self.hours = jsonData.get('hours')
        self.notes = jsonData.get('notes')
        self.address = jsonData.get('address')
        self.geocode = jsonData.get('geocode')

    def toDict(self):
        returnDict = {}
        returnDict['_id'] = self.atmId
        returnDict['name'] = self.name
        returnDict['phone_number'] = self.phone_number
        returnDict['address'] = self.address
        returnDict['notes'] = self.notes
        returnDict['hours'] = self.hours
        returnDict['geocode'] = self.geocode
        return returnDict
