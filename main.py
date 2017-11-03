from accountRequests import AccountRequests
from Model.account import Account

def main():
    accReq = AccountRequests("e7131ca32d226c905701fcca6ab9ad13")

    print("===All Accounts===")
    accounts = accReq.getAllAccounts()
    for account in accounts:
        print(account.__dict__)

    print("===Account By Id===")
    first = accounts[0]
    print(accReq.getAccount(first._id).__dict__)

    print("Account By Customer Id")
    customerId = first.customer_id
    accounts = accReq.getCustomerAccounts(customerId)
    for account in accounts:
        print(account.__dict__)

    print("Create Account For Customer")
    newAcc = accReq.createCustomerAccount(customerId, "Savings", "Name1234", 0, 0)
    print(newAcc.__dict__)
    
    print("Update Account By Id")
    accReq.updateAccount(first._id, "BestNickName")
    print(accReq.getAccount(first._id).__dict__)

    print("Delete Account By Id")
    accReq.deleteAccount(first._id)
    print("Deleted account id ", first._id)

    print("===All Accounts===")
    accounts = accReq.getAllAccounts()
    for account in accounts:
        print(account.__dict__)

if __name__ == '__main__':
    main()