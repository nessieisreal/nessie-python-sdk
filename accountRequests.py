import requests, json, urlConstants
from Model.account import Account

class AccountRequests:
    def __init__(self, apiKey):
        self.key = apiKey

    def getAllAccounts(self, accountType=None):
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
        return accounts

    def getAccount(self, accountId):
        header = {"Content-Type": "application/json"}
        payload = {"key": self.key}
        r = requests.get(urlConstants.ACCOUNTS_ID_URL % accountId, headers=header, params=payload)
        return Account.fromJson(r.json())

    def getCustomerAccounts(self, customerId):
        header = {"Content-Type": "application/json"}
        payload = {"key": self.key}
        r = requests.get(urlConstants.CUSTOMERS_ID_URL % customerId, headers=header, params=payload)
        data = r.json()
        accounts = []
        for account in data:
            accounts.append(Account.fromJson(account))
        return accounts

    def createCustomerAccount(self, customerId, type, nickname, rewards, balance, account_number=None):
        header = {"Content-Type": "application/json"}
        payload = {"key": self.key}
        if not Account.typeIsValid(type):
            raise ValueError("Account type is '{}', but it must be one of: {}".format(type, str(Account.TYPES)))
        body = {
            "type": type,
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
            raise Exception(r.text)
        return Account.fromJson(data.get("objectCreated"))

    def updateAccount(self, accountId, nickname, account_number=None):
        header = {"Content-Type": "application/json"}
        payload = {"key": self.key}
        body = {"nickname": nickname}
        if account_number is not None:
            if not Account.accountNumberIsValid(account_number):
                raise ValueError("Account number '{}' must be 16 digits".format(account_number))
            body["account_number"] = account_number
        r = requests.put(urlConstants.ACCOUNTS_ID_URL % accountId, headers=header, params=payload, data=json.dumps(body))
        data = r.json()
        if data.get("code") != 202:
            raise Exception(r.text)

    def deleteAccount(self, accountId):
        header = {"Content-Type": "application/json"}
        payload = {"key": self.key}
        r = requests.delete(urlConstants.ACCOUNTS_ID_URL % accountId, headers=header, params=payload)
