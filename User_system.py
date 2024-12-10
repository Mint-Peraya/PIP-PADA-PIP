import csv


class Account:
    account_number_counter = 1000

    def __init__(self, username, email, password, score=0):
        self.username = username
        self.email = email
        self.password = password
        Account.account_number_counter += 1
        self.account_number = Account.account_number_counter
        self.score = score
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account {account.account_number} added to user {self.username}")

    def remove_account(self, account_number):
        self.accounts = [acc for acc in self.accounts if acc.account_number != account_number]
        print(f"Account {account_number} removed from user {self.username}")

    def get_accounts(self):
        return self.accounts

    def add_score(self, amount):
        if amount > 0:
            self.score += amount

    def all_information(self):
        return [self.account_number, self.username, self.email,self.password, self.score]



