
from .exceptions import NessieApiError, IdValidationError
from ..models.address import Address
from . import constants

def validate_path(id_string: str):
    if len(id_string) != 24:
        raise IdValidationError(id_string)
    try:
        int(id_string, 16)
    except ValueError:
        raise IdValidationError(id_string)

def __is_valid_state(state: str):
    if state in constants.states:
        return constants.success
    else:
        return constants.addressInvalidState

def validate_address(address: Address):
    if address is None:
        return constants.addressMissingField
    elif re.fullmatch(r"^[0-9]{5}$", address.zipcode) is None:
        return constants.addressValidationZipCode
    elif len(address.state) != 2:
        return constants.addressNotTwoChars
    elif __is_valid_state(address.state) != constants.success:
        return constants.addressInvalidState
    return constants.success

def validate_geocode(geocode):
    if geocode is None:
        return constants.success

    lat = geocode.get('lat')
    lng = geocode.get('lng')

    if lat is None or lng is None:
        return constants.geocodeMissingFields
    if len(geocode) > 2:
        return constants.geocodeUnrecognizedField
    if lat < -90 or lat > 90 or lng < -180 or lng > 180:
        return constants.geocodeInvalidCoordinates

    return constants.success