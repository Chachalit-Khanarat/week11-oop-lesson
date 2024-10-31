from textwrap import indent


class AccountDB:
    def __init__(self):
        self.account_database = []

    def get_data(self):
        return self.account_database
    
    def insert(self, new):
        if self.search_pv(new.acc_num):
            (self.account_database).append(new)
            return True

        print("Account", new.acc_num, "already exists")
        return False
        
    def search_pup(self, acc_num):
        for i in range(len(self.account_database)):
            if self.account_database[i].acc_num == acc_num:
                return self.account_database[i]
        return False
    
    def deposit(self, acc_num, amount):
        acc = self.search_pup(acc_num)
        if not acc:
            print(acc_num, "invalid account number; no deposit action performed.")
            return False
        print("Depositing", amount, "to", acc_num)
        acc.acc_init_balance += amount

    def withdraw(self, acc_num, amount):
        acc = self.search_pup(acc_num)

        if not acc:
            print(acc_num, "invalid account number; no withdrawal action performed.")
            return False
        
        if acc.acc_init_balance >= amount:
            print("Withdrawing", amount, "from", acc_num)
            acc.acc_init_balance -= amount
            return True
        print("withdrawal amount", amount, "exceeds the balance of",
                acc.acc_init_balance, "for", acc_num, "account.")
        return False


    def search_pv(self, acc_num_new):
        for i in range(len(self.account_database)):
            if self.account_database[i].acc_num == acc_num_new:
                return False
        return True
    
    def acc_delete(self, acc_num):
        acc = self.search_pup(acc_num)
        if acc:
            print("Deleting account:", acc_num)
            self.account_database.pop(self.account_database.index(acc))
            return True
        print(acc_num, "invalid account number; nothing to be deleted.")



class Account:
    def __init__(self, acc_num, acc_type, acc_name, acc_init_balance):
        self.acc_num = acc_num
        self.acc_type = acc_type
        self.acc_name = acc_name
        self.acc_init_balance = acc_init_balance

    def __str__(self):
        return '{' + str(self.acc_num) + ',' + str(self.acc_type) + ',' + str(self.acc_name) + ',' + str(self.acc_init_balance) + '}'



acc1 = Account("001", "idk", "haha", 2000)
acc2 = Account("002", "idke", "hehe", 5000)
accdb = AccountDB()
accdb.insert(acc1)
accdb.insert(acc2)
accdb.deposit("001", 50)
print(accdb.search_pup("001"))
accdb.acc_delete("001")
accdb.acc_delete("002")
print(accdb.search_pup("001"))
print(accdb.search_pup("002"))

















# def deposit(account_num, amount):
#     index = search_account_db(account_num)
#     if index != -1:
#         print("Depositing", amount, "to", account_database[index]["account_number"])
#         account_database[index]["balance"] += amount
#     else:
#         print(account_num, "invalid account number; no deposit action performed.")

# def withdraw(account_num, amount):
#     index = search_account_db(account_num)
#     if index != -1:
#         if account_database[index]["balance"] >= amount:
#             print("Withdrawing", amount, "from", account_database[index]["account_number"])
#             account_database[index]["balance"] -= amount
#         else:
#             print("withdrawal amount", amount, "exceeds the balance of", account_database[index]["balance"], "for", account_num, "account.")
#     else:
#         print(account_num, "invalid account number; no withdrawal action performed.")
        
# def show_account(account_num):
#     index = search_account_db(account_num)
#     if index != -1:
#         print("Showing details for", account_database[index]["account_number"])
#         print(account_database[index])
#     else:
#         print(account_num, "invalid account number; nothing to be shown for.")

# create_account("0000", "saving", "David Patterson", 1000)
# create_account("0001", "checking", "John Hennessy", 2000)
# create_account("0003", "saving", "Mark Hill", 3000)
# create_account("0004", "saving", "David Wood", 4000)
# create_account("0004", "saving", "David Wood", 4000)
# print(account_database)
# show_account('0003')
# deposit('0003', 50)
# show_account('0003')
# withdraw('0003', 25)
# show_account('0003')
# delete_account('0003')
# show_account('0003')
# deposit('0003', 50)
# withdraw('0001', 6000)
