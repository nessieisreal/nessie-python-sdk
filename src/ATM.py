import requests

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

class ATMRequest(object):

    def __init__(self, apiKey):
        self.baseUrl = 'http://api.reimaginebanking.com'
        self.key = apiKey

    def __buildParams(self, lat, lng, rad):
        param = {'key': self.key}
        if (lat == None):
            param['lat'] = lat
        if (lng == None):
            param['lng'] = lng
        if (rad == None):
            param['rad'] = rad
        return param

    def __formatResponse(self, json):
        respList = []
        for atm in json['data']:
            respList.append(ATM(atm))
        return respList

    def getAtms(self, lat=None, lng=None, rad=None):
        reqUrl = "%s/atms" % self.baseUrl
        par = self.__buildParams(lat, lng, rad)

        r = requests.get(reqUrl, params=par)
        if r.status_code != 200:
            return (None, r.json())

        jsonAtms = r.json()

        while ('next' in r.json()['paging']):
            reqUrl = "%s%s" % (self.baseUrl, r.json()['paging']['next'])
            r = requests.get(reqUrl)

            if r.status_code != 200:
                return (None, r.json())

            jsonAtms['data'] = jsonAtms['data'] + r.json()['data']

        return (self.__formatResponse(jsonAtms), None)

    def getAtmById(self, idCode):
        reqUrl = "%s/atms/%s" % (self.baseUrl, idCode)
        par = {'key': self.key}

        r = requests.get(reqUrl, params=par)
        if r.status_code != 200:
            return (None, r.json())
        
        return (ATM(r.json()), None)



def main():

    apiKey = input("Please enter in your Nessie API Key: ")
    client = ATMRequest(apiKey)
    # atms = client.getAtms()[0]

    # print(atms[0].atmId)
    arlingtonAtm = client.getAtmById('56c66be5a73e492741506f2b')[0]
    print(arlingtonAtm.address)

if __name__ == "__main__":
    main()