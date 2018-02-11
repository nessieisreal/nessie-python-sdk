import requests, json, urlConstants
from .models.account import Account
from .utils.exceptions import NessieApiError

class AccountRequest:
    def __init__(self, apiKey):
        self.key = apiKey

    def get_all_accounts(self, accountType=None):
        header = {"Content-Type": "application/json"}
        payload = {"key": self.key}
        if accountType is not None:
            if not Account.typeIsValid(accountType):
                raise ValueError("accountType must be one of: {}".format(str(Account.TYPES)))
            payload["type"] = accountType
        r = requests.get(urlConstants.ACCOUNTS_URL, headers=header, params=payload)
        data = r.json()
        accounts = []
        for account in data:
            accounts.append(Account.fromJson(account))
        if r.status_code != 200:
            raise NessieApiError(r)
        return accounts

    def get_account(self, accountId):
        header = {"Content-Type": "application/json"}
        payload = {"key": self.key}
        r = requests.get(urlConstants.ACCOUNTS_ID_URL % accountId, headers=header, params=payload)
        if r.status_code != 200:
            raise NessieApiError(r)
        return Account.fromJson(r.json())

    def get_customer_accounts(self, customerId):
        header = {"Content-Type": "application/json"}
        payload = {"key": self.key}
        r = requests.get(urlConstants.CUSTOMERS_ID_URL % customerId, headers=header, params=payload)
        data = r.json()
        if r.status_code != 200:
            raise NessieApiError(r)
        accounts = []
        for account in data:
            accounts.append(Account.fromJson(account))
        return accounts

    def create_customer_account(self, customerId, account_type, nickname, rewards, balance, account_number=None):
        header = {"Content-Type": "application/json"}
        payload = {"key": self.key}
        if not Account.typeIsValid(account_type):
            raise ValueError("Account type is '{}', but it must be one of: {}".format(account_type, str(Account.TYPES)))
        body = {
            "type": account_type,
            "nickname": nickname,
            "rewards": rewards,
            "balance": balance
        }
        if account_number is not None:
            if not Account.accountNumberIsValid(account_number):
                raise ValueError("Account number '{}' must be 16 digits".format(account_number))
            body["account_number"] = account_number
        r = requests.post(urlConstants.CUSTOMERS_ID_URL % customerId, headers=header, params=payload, data=json.dumps(body))
        data = r.json()
        if data.get("code") != 201:
            raise NessieApiError(r)
        return Account.fromJson(data.get("objectCreated"))

    def update_account(self, accountId, nickname, account_number=None):
        header = {"Content-Type": "application/json"}
        payload = {"key": self.key}
        body = {"nickname": nickname}
        if account_number is not None:
            if not Account.accountNumberIsValid(account_number):
                raise ValueError("Account number '{}' must be 16 digits".format(account_number))
            body["account_number"] = account_number
        r = requests.put(urlConstants.ACCOUNTS_ID_URL % accountId, headers=header, params=payload, data=json.dumps(body))
        data = r.json()
        # TODA: probably need to change nessier api error to
        # NessierApiError(r)
        if data.get("code") != 202:
            raise NessieApiError(r.text)

    def delete_account(self, accountId):
        header = {"Content-Type": "application/json"}
        payload = {"key": self.key}
        r = requests.delete(urlConstants.ACCOUNTS_ID_URL % accountId, headers=header, params=payload)
        data = r.json()
        if data.get("code") != 202:
            raise NessieApiError(r.text)
