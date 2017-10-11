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

#Codes: 1 denotes that one but not all of the fields were used
#Codes: 2 denotes that the lat or lng value was invalid (e.g. lat greater than 90)
class ATMValidationError(Exception):
    def __init__(self, message, code):
        super(ATMValidationError, self).__init__(message)
        self.code = code

class ATMRequest(object):

    def __init__(apiKey):
        self.baseUrl = 'http://api.reimaginebanking.com'
        self.key = apiKey

    def validateLatLngRad(lat, lng, rad):
        if lat == None and lng == None and rad == None:
            return
        if lat is not None and lng is not None and rad is not None:
            if lat > 90 or lat < -90 or lng > 180 or lng < -180:
                raise ATMValidationError("Latitude or longitude coordinate is invalid", 2)
        else:
            raise ATMValidationError("At least one ATM field is used but not all", 1)

    def buildParams(lat, lng, rad):
        param = {'key': self.key}
        if (lat == None or lng == None or rad == None):
            return param
        param['lat'] = lat
        param['lng'] = lng
        param['rad'] = rad
        return param

    def formatResponse(json):
        respList = []
        for atm in respDict['data']:
            respList.append(ATM(atm))
        return respList

    def getAtms(lat=None, lng=None, rad=None, pages=0):
        self.validateLatLngRad(lat, lng, rad)
        reqUrl = "%s/atms" % self.baseUrl
        par = self.buildParams(lat, lng, rad)

        r = requests.get(reqUrl, params=par)

        if r.status_code != 200:
            return (None, r.json())

        jsonAtms = r.json()
        pageNum = 1

        while (pageNum < pages or pages == 0 and 'next' in r.json()['paging']):
            reqUrl = "%s%s" % (self.baseUrl, r.json()['paging']['next'])
            print reqUrl
            r = requests.get(reqUrl)

            if r.status_code != 200:
                return (None, r.json())

            jsonAtms['data'] = jsonAtms['data'] + r.json()['data']

        return (self.formatResponse(jsonAtms), None)