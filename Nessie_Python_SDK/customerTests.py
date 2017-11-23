from customerRequests import CustomerRequests
from models.address import Address

custReq = CustomerRequests('5b7b8b56912ea2263c782a77adf33a92')
custAddress = Address("1234", "Randolph Street", "Vienna", "VA", "64738")
createdCustomer = custReq.createCustomer("Automated", "Test", custAddress)
assert createdCustomer.first_name == "Automated"
assert createdCustomer.last_name == "Test"
assert createdCustomer.address.street_number == "1234"
assert createdCustomer.address.street_name == "Randolph Street"
assert createdCustomer.address.city == "Vienna"
assert createdCustomer.address.state == "VA"
assert createdCustomer.address.zipcode == "64738"
assert createdCustomer.customer_id is not None
custID = createdCustomer.customer_id

newAddress = Address("4321", "Quincy Street", "Tysons", "VA", "54325")
updatedCustomer = custReq.updateCustomer(custID, newAddress)
assert updatedCustomer is True

allCustomers = custReq.getAllCustomers()

getCustomer = custReq.getCustomerById(custID)
assert getCustomer.first_name == "Automated"
assert getCustomer.last_name == "Test"
assert getCustomer.address.street_number == "4321"
assert getCustomer.address.street_name == "Quincy Street"
assert getCustomer.address.city == "Tysons"
assert getCustomer.address.state == "VA"
assert getCustomer.address.zipcode == "54325"
assert getCustomer.customer_id == custID

# TODO: getCustomerByAccountId when account is done
# accountCustomer = custReq.getCustomerByAccountId("59fbf40fb390353c953a1b8e")
# print(accountCustomer.firstName, accountCustomer.lastName, accountCustomer.customerId, )
