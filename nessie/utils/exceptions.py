from . import constants

class ATMValidationError(Exception):
    def __init__(self, code):
        if code == constants.atmMissingFields:
            message = 'Request is missing one or more of the following fields: lat, lng, rad. Request must have all or none of these fields.'
        elif code == constants.atmInvalidFields:
            message = \
                'Request contains invalid fields. Lat must be between -90 and 90. Lng must be between -180 and 180.'
        else:
            message = 'Unrecognized Error'
        super(ATMValidationError, self).__init__(message)

class IdValidationError(Exception):
    def __init__(self, id_code):
        id_len = len(id_code)
        if id_len != 24:
            message = 'User provided the following _id with %d characters: %s. IDs have 24 characters' % (id_len, id_code)
        else:
            message = 'User provided the following ID: %s. The provided ID is not a valid hexidecimal number' % (id_code)
        super(IdValidationError, self).__init__(message)

class MerchantValidationError(Exception):
    def __init__(self, code):
        if code == constants.merchantMissingGetterFields:
            message = 'Request is missing one or more of the following fields: lat, lng, rad. Request must have all or none of these fields.'
        elif code == constants.merchantInvalidFields:
            message = 'Request contains invalid fields. Lat must be between -90 and 90. Lng must be between -180 and 180.'
        elif code == constants.merchantMissingCreateFields:
            message = 'Request is missing one or more of the following fields: name, category, address, geocode'
        else:
            message = 'Unrecognized Error'
        super(MerchantValidationError, self).__init__(message)


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
        elif code == constants.addressNotTwoChars:
            message = 'Address has invalid state field. States must be in the form of the two-character postal abbreviation'
        else:
            message = 'Unrecognized Error'
        super(AddressValidationError, self).__init__(message)

class GeocodeValidationError(Exception):
    def __init__(self, code):
        if code == constants.geocodeMissingFields:
            message = 'Geocode lacks either lat or lng fields.'
        elif code == constants.geocodeUnrecognizedField:
            message = 'Geocode dict contains one or more fields athat are not \'lat\' or \'lng\'.'
        elif code == constants.geocodeInvalidCoordinates:
            message = 'Geocode coordinates are malformed. Lat must be between -90 and 90. Lng must be between -180 and 180.'
        else:
            message = 'Unrecognized Error'

        super(GeocodeError, self).__init__(message)
