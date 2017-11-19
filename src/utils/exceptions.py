import utils.constants

class ATMValidationError(Exception):
    def __init__(self, code):
        message = ''
        if (code == constants.missingFields):
            message = 'Request is missing one or more of the following fields: lat, lng, rad.'
        elif(code == constants.invalidFields):
            message = 'Request contains invalid fields. Lat must be between -90 and 90. Lng must be between -180 and 180.'
        else:
            'Unrecognized Error'
        super(ATMValidationError, self).__init__(message)

class NessieApiError(Exception):
    def __init__(self, response):
        self.code = response.status_code
        super(NessieApiError, self).__init__(response.text)
