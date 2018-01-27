import requests
import json
import re

from nessie.models.merchant import Merchant
from nessie.utils.exceptions import NessieApiError, AddressValidationError

class MerchantRequests:

    def __init__(self, api_key):
        self.key = api_key

    