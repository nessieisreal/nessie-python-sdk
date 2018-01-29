import requests
import json
import re

from models.merchant import Merchant
from utils.exceptions import NessieApiError, AddressValidationError, MerchantValidationError
from utils import constants 

class MerchantRequest:

    def __init__(self, api_key):
        self.key = api_key

    def __buildParams(self, lat, lng, rad):
        param = {'key': self.key}
        if (lat != None):
            param['lat'] = lat
        if (lng != None):
            param['lng'] = lng
        if (rad != None):
            param['rad'] = rad
        return param

    def __validateParams(self, req):
        lat = req.get('lat')
        lng = req.get('lng')
        rad = req.get('rad')
        
        paramsExist = lat is not None or lng is not None or rad is not None
        paramsMissing = lat is None or lng is None or rad is None
        paramsInvalid = not paramsMissing and (lat < -90 or lat > 90 or lng < -180 or lng > 180 or rad <= 0)
        
        if (paramsExist and paramsMissing):
            raise MerchantValidationError(constants.merchantMissingFields)
        if (paramsInvalid):
            raise MerchantValidationError(constants.merchantInvalidFields)

    def __format_response(self, json_array):
        resp_list = []
        for merchant_dict in json_array:
            resp_list.append(Merchant(merchant_dict))
        return resp_list

    def get_all_merchants(self, lat=None, lng=None, rad=None):
        par = self.__buildParams(lat, lng, rad)
        self.__validateParams(par)
        header = {'Content-Type': 'application/json'}

        print(constants.merchantsUrl)

        r = requests.get(constants.merchantsUrl, headers=header, params=par)
        if r.status_code != constants.httpOk:
            raise NessieApiError(r)

        merchant_list = r.json()

        # for merch in merchant_list:
        #     print(merch)

        return self.__format_response(merchant_list)


def main():
    print('Import this class to use Nessie\'s Merchant APIs!')
    api_key = '6d710f1c84683f0aa00f8888e12a9e59'

    req = MerchantRequest(api_key)
    mers = req.get_all_merchants()

    for mer in mers:
        print(mer.to_dict())
    
    
if __name__ == '__main__':
    main()
