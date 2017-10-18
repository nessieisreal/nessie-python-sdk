class ATM(object):

    def __init__(self, jsonData):
        if '_id' in jsonData:
            self.atmId = jsonData['_id']
        else:
            self.atmId = None
        if 'name' in jsonData:
            self.name = jsonData['name']
        else:
            self.name = None
        if 'language_list' in jsonData:
            self.langList = jsonData['language_list']
        else:
            self.langList = None
        if 'address' in jsonData:
            self.address = jsonData['address']
        else:
            self.address = None
        if 'amount_left' in jsonData:
            self.amountLeft = jsonData['amount_left']
        else:
            self.amountLeft = None
        if 'accessibility' in jsonData:
            self.accessibility = jsonData['accessibility']
        else:
            self.accessibility = None
        if 'hours' in jsonData:
            self.hours = jsonData['hours']
        else:
            self.hours = None
        if 'geocode' in jsonData:
            geocode = {}
            if 'lat' in jsonData['geocode']:
                geocode['lat'] = jsonData['geocode']['lat']
            else:
                geocode['lat'] = None
            if 'lng' in jsonData['geocode']:
                geocode['lng'] = jsonData['geocode']['lng']
            else:
                geocode['lng'] = None
            self.geocode = geocode
        else:
            self.geocode = None

    def toDict(self):
        returnDict = {}
        returnDict['_id'] = self.atmId
        returnDict['name'] = self.name
        returnDict['language_list'] = self.langList
        returnDict['address'] = self.address
        returnDict['amount_left'] = self.amountLeft
        returnDict['accessibility'] = self.accessibility
        returnDict['hours'] = self.hours
        returnDict['geocode'] = self.geocode
        return returnDict

print("HELLO")