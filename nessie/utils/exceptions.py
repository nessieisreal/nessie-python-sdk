from nessie import utils

class ATMValidationError(Exception):
    def __init__(self, code):
        if code == constants.atmMissingFields:
            message = 'Request is missing one or more of the following fields: lat, lng, rad.'
        elif code == constants.atmInvalidFields:
            message = \
                'Request contains invalid fields. Lat must be between -90 and 90. Lng must be between -180 and 180.'
        else:
            message = 'Unrecognized Error'
        super(ATMValidationError, self).__init__(message)

class BranchValidationError(Exception):
    def __init__(self, id_code):
        id_len = len(id_code)
        if id_len != 24:
            message = 'User provided the following branch ID with %d characters: %s. Branch IDs have 24 characters' % (id_len, id_code)
        else:
            message = 'User provided the following branch ID: %s. The provided ID is not a valid hexidecimal number' % (id_code)
        super(BranchValidationError, self).__init__(message)


class NessieApiError(Exception):
    def __init__(self, response):
        self.code = response.status_code
        super(NessieApiError, self).__init__(response.text)


class CustomerValidationError(Exception):
    def __init__(self, code):
        if code == constants.createCustomerMissingFields:
            message = 'Request is missing one or more of the following fields: first_name, last_name.'
        elif code == constants.customerIdMissingField:
            message = 'Request is missing the identification number field.'
        else:
            message = 'Unrecognized Error'
        super(CustomerValidationError, self).__init__(message)


class AddressValidationError(Exception):
    def __init__(self, code):
        if code == constants.addressMissingField:
            message = 'Request is missing the address field.'
        elif code == constants.addressValidationZipCode:
            message = 'Address has an invalid zip code. The zip code must be a number with 5 digits.'
        else:
            message = 'Unrecognized Error'
        super(AddressValidationError, self).__init__(message)
