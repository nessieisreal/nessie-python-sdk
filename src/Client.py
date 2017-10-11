import requests
from ATM import ATM, ATMRequest

# My Key: "6d710f1c84683f0aa00f8888e12a9e59"

class NessieClient(object):
    def __init__(self, apiKey):
        self.key = apiKey
        self.baseUrl = 'http://api.reimaginebanking.com'
        self.baseEnterpriseUrl = '%s/enterprise' % self.baseUrl
    def getKey():
        if self.key == "":
            print("No key is present. An api key is required to send requests")
        return self.key
    def setKey(apiKey):
        self.key = apiKey

    # Methods Dealing With ATMS

    def getAtms(lat=None, lng=None, rad=None, pages=0):
        return ATMRequest(self.key).getAtms(lat, lng, rad, pages)

def main():
    client = NessieClient("6d710f1c84683f0aa00f8888e12a9e59")
    myLat = 38.9283
    myLng = -77.1753
    myRad = 10

    atmData = client.getAtms(lat=myLat, lng=myLng, rad=myRad)
    print(atmData)

if __name__ == '__main__':
    main()