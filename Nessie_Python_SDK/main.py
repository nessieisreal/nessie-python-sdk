from customerRequests import CustomerRequests
from Model.address import Address

custReq = CustomerRequests('5b7b8b56912ea2263c782a77adf33a92')
custAddress = Address("1234", "Randolph Street", "Vienna", "VA", "64738")
createdCustomer = custReq.createCustomer("python", "test", custAddress)
custID = createdCustomer.getCustomerId()
newAddress = Address("4321", "Quincy Street", "Tysons", "VA", "54325")
updatedCustomer = custReq.updateCustomer(custID, newAddress)
print(updatedCustomer)
allCustomers = custReq.getAllCustomers()
getCustomer = custReq.getCustomerById(custID)
print(getCustomer.getCustomerId())