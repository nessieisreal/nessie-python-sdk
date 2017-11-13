import requests
from models.atm import ATM
import utils.constants
from utils.validationExceptions import ATMValidationError, ATMClientError

class ATMRequest(object):

    def __init__(self, apiKey):
        self.baseUrl = utils.constants.baseUrl
        self.key = apiKey

    def __buildParams(self, lat, lng, rad):
        param = {'key': self.key}
        if (lat != None):
            param['lat'] = lat
        if (lng != None):
            param['lng'] = lng
        if (rad != None):
            param['rad'] = rad
        return param

    def __formatResponse(self, json):
        respList = []
        for atm in json['data']:
            respList.append(ATM(atm))
        return respList

    def __validateParams(self, req):
        lat = req.get('lat')
        lng = req.get('lng')
        rad = req.get('rad')

        if (lat is not None or lng is not None or rad is not None):
            if (lat is None or lng is None or rad is None):
                raise ATMValidationError(utils.constants.missingFields)
            if (lat < -90 or lat > 90 or lng < -180 or lng > 180):
                raise ATMValidationError(utils.constants.invalidFields)


    def getAtms(self, lat=None, lng=None, rad=None):
        reqUrl = "%s/atms" % self.baseUrl
        par = self.__buildParams(lat, lng, rad)
        self.__validateParams(par)

        r = requests.get(reqUrl, params=par)
        if r.status_code != 200:
            raise ATMClientError(r)

        jsonAtms = r.json()

        while ('next' in r.json()['paging']):
            reqUrl = "%s%s" % (self.baseUrl, r.json()['paging']['next'])
            r = requests.get(reqUrl)

            if r.status_code != 200:
                raise ATMClientError(r)

            jsonAtms['data'] = jsonAtms['data'] + r.json()['data']

        return self.__formatResponse(jsonAtms)

    def getAtmById(self, idCode):
        reqUrl = "%s/atms/%s" % (self.baseUrl, idCode)
        par = {'key': self.key}

        r = requests.get(reqUrl, params=par)

        print(par)

        print('Status Code: %s' % r.status_code)
        print('Message: %s' % r.reason)

        if r.status_code != 200:
            raise ATMClientError(r)
        
        return ATM(r.json())



def main():

    apiKey = input("Please enter in your Nessie API Key: ")
    client = ATMRequest(apiKey)
    atms = client.getAtms()

    print('Id of one of the atms: %s' % atms[0].atmId)
    arlingtonAtm = client.getAtmById('56c66be5a73e492741506f2b')
    print(arlingtonAtm.address)

if __name__ == "__main__":
    main()