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

merchantMissingFields = 7
merchantInvalidFields = 8

# HTTP Status Codes
httpOk = 200
httpCreated = 201
