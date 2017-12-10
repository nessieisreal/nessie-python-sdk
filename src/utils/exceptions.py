import utils.constants

class ATMValidationError(Exception):
    def __init__(self, code):
        message = ''
        if (code == constants.missingFields):
            message = 'Request is missing one or more of the following fields: lat, lng, rad.'
        elif(code == constants.invalidFields):
            message = 'Request contains invalid fields. Lat must be between -90 and 90. Lng must be between -180 and 180.'
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
