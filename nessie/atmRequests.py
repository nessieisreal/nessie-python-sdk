import requests
from .models.atm import ATM
from .utils import constants
from .utils.exceptions import ATMValidationError, NessieApiError

class ATMRequest(object):

    def __init__(self, apiKey):
        self.baseUrl = constants.baseUrl
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
        
        paramsExist = lat is not None or lng is not None or rad is not None
        paramsMissing = lat is None or lng is None or rad is None
        paramsInvalid = not paramsMissing and (lat < -90 or lat > 90 or lng < -180 or lng > 180 or rad <= 0)
        
        if (paramsExist and paramsMissing):
            raise ATMValidationError(constants.atmMissingFields)
        if (paramsInvalid):
            raise ATMValidationError(constants.atmInvalidFields)
            
    def get_atms(self, lat=None, lng=None, rad=None):
        reqUrl = "%s/atms" % self.baseUrl
        par = self.__buildParams(lat, lng, rad)
        self.__validateParams(par)

        r = requests.get(reqUrl, params=par)
        if r.status_code != 200:
            raise NessieApiError(r)

        jsonAtms = r.json()
        while ('next' in r.json()['paging']):
            print(r.json())
            reqUrl = "%s%s" % (self.baseUrl, r.json()['paging']['next'])
            r = requests.get(reqUrl)

            if r.status_code != 200:
                raise NessieApiError(r)

            jsonAtms['data'] = jsonAtms['data'] + r.json()['data']

        return self.__formatResponse(jsonAtms)

    def get_atm(self, idCode):
        reqUrl = "%s/atms/%s" % (self.baseUrl, idCode)
        par = {'key': self.key}

        r = requests.get(reqUrl, params=par)

        if r.status_code != 200:
            raise NessieApiError(r)
        
        return ATM(r.json())



def main():
    print("Import this class to use Nessie's ATM APIs!")

if __name__ == "__main__":
    main()
