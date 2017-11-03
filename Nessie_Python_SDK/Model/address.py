class Address:
	def __init__(self, streetNumber: str, streetName: str, city: str, state: str, zipcode: str):
		self.streetNumber = streetNumber
		self.streetName = streetName
		self.city = city
		self.state = state
		self.zipcode = zipcode

	def createDict(self):
		return {
			"street_number" : self.streetNumber,
			"street_name" : self.streetName,
			"city" : self.city,
			"state" : self.state,
			"zip" : self.zipcode
			}