import requests
import json
from nessie.utils import constants
from nessie.models.loan import Loan
from nessie.utils.exceptions import NessieApiError


class LoanRequests:

    def __init__(self, api_key):
        self.base_url = constants.baseUrl
        self.api_key = api_key
        self.header = {"Content-Type": "application/json"}

        self.__loan_types__ = constants.LOAN_TYPES
        self.__status_types__ = constants.LOAN_STATUS

    def get_account_loans(self, account_id):
        url = self.base_url + "/accounts/{id}/loans?key={key}".format(id=account_id, key=self.api_key)
        response = requests.get(url, headers=self.header)

        if response.status_code >= 300:
            raise NessieApiError(response)

        account_loans = []
        for loan in response.json():
            account_loans.append(Loan(loan))

        if len(account_loans) == 0:
            print("No loans found in account {0}".format(account_id))
            print("Returning empty list.")

        return account_loans

    def get_loan_by_id(self, loan_id):
        url = self.base_url + "/loans/{id}?key={key}".format(id=loan_id, key=self.api_key)
        response = requests.get(url, headers=self.header)

        if response.status_code >= 300:
            raise NessieApiError(response)

        return Loan(response.json())

    def create_loan(self, account_id, loan_type, status, credit_score, monthly_payment, amount, description=None):
        if loan_type.lower() not in self.__loan_types__:
            raise ValueError("User specified Loan Type '{user_loan}' not in list of valid loan types '{valid}'."
                             .format(user_loan=loan_type, valid=self.__loan_types__))
        if status.lower() not in self.__status_types__:
            raise ValueError("User specified Loan Status '{user_loan}' not in list of valid loan statuses '{valid}'."
                             .format(user_loan=loan_type, valid=self.__status_types__))
        payload = {
            "type": loan_type.lower(),
            "status": status.lower(),
            "credit_score": credit_score,
            "monthly_payment": monthly_payment,
            "amount": amount
        }
        if description is not None:
            payload["description"] = description

        url = self.base_url + "/accounts/{acct_id}/loans?key={key}".format(acct_id=account_id, key=self.api_key)
        response = requests.post(url, headers=self.header, data=json.dumps(payload))

        if response.status_code >= 300:
            raise NessieApiError(response)
        return Loan(response.json()['objectCreated'])

    def update_loan(self, loan_id, loan_type=None, status=None, credit_score=None, monthly_amount=None, amount=None, description=None):
        arguments = locals()
        arguments.pop("self")
        arguments.pop("loan_id")
        # Change the name of loan_type to type. Cannot use 'type' in args as it is an internal python function
        arguments['type'] = arguments.pop("loan_type")
        payload = {}
        for arg in arguments.items():
            if arg[1] is not None:
                payload[arg[0]] = arg[1]
        url = self.base_url + "/loans/{id}?key={key}".format(id=loan_id, key=self.api_key)
        response = requests.put(url, headers=self.header, data=json.dumps(payload))
        if response.status_code >= 300:
            raise NessieApiError(response)

        return response.json()

    def delete_loan(self, loan_id):
        url = self.base_url + "/loans/{id}?key={key}".format(id=loan_id, key=self.api_key)
        response = requests.delete(url)
        if response.status_code >= 300:
            raise NessieApiError(response)
        return








