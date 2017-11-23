from customerRequests import CustomerRequests
from models.address import Address

custReq = CustomerRequests('5b7b8b56912ea2263c782a77adf33a92')
custAddress = Address("1234", "Randolph Street", "Vienna", "VA", "64738")
createdCustomer = custReq.createCustomer("Automated", "Test", custAddress)
assert createdCustomer.firstName == "Automated"
assert createdCustomer.lastName == "Test"
assert createdCustomer.address.streetNumber == "1234"
assert createdCustomer.address.streetName == "Randolph Street"
assert createdCustomer.address.city == "Vienna"
assert createdCustomer.address.state == "VA"
assert createdCustomer.address.zipcode == "64738"
assert createdCustomer.customerId is not None
custID = createdCustomer.customerId

newAddress = Address("4321", "Quincy Street", "Tysons", "VA", "54325")
updatedCustomer = custReq.updateCustomer(custID, newAddress)
assert updatedCustomer == True

allCustomers = custReq.getAllCustomers()

getCustomer = custReq.getCustomerById(custID)
assert getCustomer.firstName == "Automated"
assert getCustomer.lastName == "Test"
assert getCustomer.address.streetNumber == "4321"
assert getCustomer.address.streetName == "Quincy Street"
assert getCustomer.address.city == "Tysons"
assert getCustomer.address.state == "VA"
assert getCustomer.address.zipcode == "54325"
assert getCustomer.customerId == custID

# TODO: getCustomerByAccountId when account is done
# accountCustomer = custReq.getCustomerByAccountId("59fbf40fb390353c953a1b8e")
# print(accountCustomer.firstName, accountCustomer.lastName, accountCustomer.customerId, )
