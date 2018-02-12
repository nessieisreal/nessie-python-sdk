import requests
import json
import re

from models.merchant import Merchant
from models.address import Address
from utils.exceptions import NessieApiError, AddressValidationError, MerchantValidationError, GeocodeValidationError
from utils import constants 
from utils.validation import validate_path, validate_address, validate_geocode

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
            raise MerchantValidationError(constants.merchantMissingGetterFields)
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

        return self.__format_response(merchant_list)

    def get_merchant_by_id(self, id):
        validate_path(id)
        header = {'Content-Type': 'application/json'}
        par = {'key': self.key}
        url = constants.merchantsUrl + "/" + id

        r = requests.get(url, headers=header, params=par)
        if r.status_code != constants.httpOk:
            raise NessieApiError(r)

        return Merchant(r.json())

    def create_merchant(self, name: str, category: str, address: Address, geocode):
        if (name is None or category is None or address is None):
            raise MerchantValidationError(constants.merchantMissingCreateFields)
        geocode_validate_code = validate_geocode(geocode)
        if geocode_validate_code != constants.success:
            raise GeocodeValidationError(geocode_validate_code)
            
        
        addr_validate_code = validate_address(address)
        if (addr_validate_code != constants.success or addr_validate_code != constants.addressInvalidState):
            raise AddressValidationError(addr_validate_code)
        elif (addr_validate_code == constants.addressInvalidState):
            print("[MerchantRequest] WARNING: State field is of a valid two-char format but does not contain a valid state abbreviation.")

        header = {"Content-Type": "application/json"}
        par = {"key": self.key}
        body = {
            "name": name,
            "category": category,
            "address": address.to_dict(),
            "geocode": geocode
        }

        r = requests.post(utils.constants.customersUrl, headers=header, params=payload, data=json.dumps(body))
        if r.status_code != 201:
            raise NessieApiError(r)

        json_data = r.json
        return Merchant(json_data.get("objectCreated"))
        

def main():
    print('Import this class to use Nessie\'s Merchant APIs!')
    api_key = '6d710f1c84683f0aa00f8888e12a9e59'

    req = MerchantRequest(api_key)
    mers = req.get_all_merchants()

    for mer in mers:
        print(mer.to_dict())

    print('Now getting merchant by id')
    _id = mers.pop().merchant_id

    merch = req.get_merchant_by_id(_id)
    print(merch.to_dict())

    print("Now attempting to post a merchant")
    name = 'George\'s House of Wares'
    category = 'Uncategorical'
    addr = Address("123", "Appian Way", "Rome", "NY", "14850")
    geocode = {"lat": 0, "lng": 0}
    creatMerch = req.create_merchant(name, category, addr, geocode)

    print(creatMerch.to_dict())
    
    
if __name__ == '__main__':
    main()
