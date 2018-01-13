# Urls
baseUrl = "http://api.reimaginebanking.com"
customersUrl = baseUrl + "/customers"
accountsUrl = baseUrl + "/accounts"
customersIdUrl = customersUrl + "/%s"
accountsCustomerIdUrl = accountsUrl + "/%s/customer"

# Exception Messages
success = 0
atmMissingFields = 1
atmInvalidFields = 2
createCustomerMissingFields = 3
customerIdMissingField = 4
addressValidationZipCode = 5
addressMissingField = 6
