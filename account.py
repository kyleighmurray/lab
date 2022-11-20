

class Account():
    '''
    Class that stores information for a bank account.
    '''
    def __init__(self, name: str):
        '''
        Constructor to create intial state of an account object.
        
        :param name: Account's name
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        '''
        Method to deposit an amount and update the account balance if possible.

        :param amount: The amount of money to be deposited
        :return: True or False to indicate whether the deposit was successful
        '''
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        '''
        Method to withdraw an amount and update the account balance if possible.

        :param amount: The amount of money to be withdrawn
        :return: True or False to indicate whether the withdrawl was successful
        '''
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        '''
        Method to access an account's balance.

        :return: Current account balance
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Method to access an account's username.

        :return: An account's name
        '''
        return self.__account_name
