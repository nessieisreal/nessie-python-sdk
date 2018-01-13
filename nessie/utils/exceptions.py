import utils.constants


class ATMValidationError(Exception):
    def __init__(self, code):
        if code == utils.constants.atmMissingFields:
            message = 'Request is missing one or more of the following fields: lat, lng, rad.'
        elif code == utils.constants.atmInvalidFields:
            message = \
                'Request contains invalid fields. Lat must be between -90 and 90. Lng must be between -180 and 180.'
        else:
            message = 'Unrecognized Error'
        super(ATMValidationError, self).__init__(message)


class NessieApiError(Exception):
    def __init__(self, response):
        self.code = response.status_code
        super(NessieApiError, self).__init__(response.text)


class CustomerValidationError(Exception):
    def __init__(self, code):
        if code == utils.constants.createCustomerMissingFields:
            message = 'Request is missing one or more of the following fields: first_name, last_name.'
        elif code == utils.constants.customerIdMissingField:
            message = 'Request is missing the identification number field.'
        else:
            message = 'Unrecognized Error'
        super(CustomerValidationError, self).__init__(message)


class AddressValidationError(Exception):
    def __init__(self, code):
        if code == utils.constants.addressMissingField:
            message = 'Request is missing the address field.'
        elif code == utils.constants.addressValidationZipCode:
            message = 'Address has an invalid zip code. The zip code must be a number with 5 digits.'
        else:
            message = 'Unrecognized Error'
        super(AddressValidationError, self).__init__(message)
