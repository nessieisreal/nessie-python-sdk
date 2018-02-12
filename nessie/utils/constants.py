# Urls
baseUrl = "http://api.reimaginebanking.com"

customersUrl = baseUrl + "/customers"
customersIdUrl = customersUrl + "/%s"

accountsUrl = baseUrl + "/accounts"
accountsCustomerIdUrl = accountsUrl + "/%s/customer"

merchantsUrl = baseUrl + "/merchants"

# Exception Messages
success = 0

atmMissingFields = 1
atmInvalidFields = 2

createCustomerMissingFields = 3
customerIdMissingField = 4

addressValidationZipCode = 5
addressMissingField = 6
addressNotTwoChars = 7
addressInvalidState = 8

merchantMissingGetterFields = 9
merchantInvalidFields = 10
merchantMissingCreateFields = 11

geocodeUnrecognizedField = 12
geocodeMissingFields = 13
geocodeInvalidCoordinates = 14

# HTTP Status Codes
httpOk = 200
httpCreated = 201

# List of State Abbrs
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]