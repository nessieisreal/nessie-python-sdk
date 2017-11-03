import requests

class ATM(object):

    def __init__(self, jsonData):
        self.atmId = jsonData.get('_id')
        self.name = jsonData.get('name')
        self.language_list = jsonData.get('language_list')
        self.address = jsonData.get('address')
        self.amount_left = jsonData.get('amount_left')
        self.accessibility = jsonData.get('accessibility')
        self.hours = jsonData.get('hours')
        self.geocode = jsonData.get('geocode')

    def toDict(self):
        returnDict = {}
        returnDict['_id'] = self.atmId
        returnDict['name'] = self.name
        returnDict['language_list'] = self.language_list
        returnDict['address'] = self.address
        returnDict['amount_left'] = self.amount_left
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