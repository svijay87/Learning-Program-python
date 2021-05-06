# Open Closed Principal

# Software entities(Classes, modules, functions) should be open for extension, not modification


class RBI:
    def __init__(self, name):
        self.bank_name = name


    def get_name(self):
        pass

    def working_hours(self):
        print('RBI working_hours function')

# OCP Approach
# Implement individual class for different categories banks
# It will helpful to extends and introduce new category bank


class GovtBank(RBI):
    def working_hours(self):
        print('10-5 - Monday to Friday')


class PrivateBank(RBI):
    def working_hours(self):
        print('10-4 - Monday to Friday and saturday half day working')


class SmallFinanceBank(RBI):
    def working_hours(self):
        print('10-4 - Monday to Saturday')


banks = [
    RBI('GovtBank'),
    RBI('PrivateBank'),
    RBI('SmallFinanceBank')
]


def banks_working_hours_old(banks: list):
    for bank in banks:
        if bank.bank_name == 'GovtBank':
            print('10-5 - Monday to Friday')
        elif bank.bank_name == 'PrivateBank':
            print('10-4 - Monday to Friday and saturday half day working')
        elif bank.bank_name == 'SmallFinanceBank':
            print('10-4 - Monday to Saturday')


def banks_working_hours(banks: list):
    for bank in banks:
        print(bank.bank_name)
        bank.working_hours()


banks_working_hours_old(banks)

banks_new = [
    GovtBank('GovtBank'),
    PrivateBank('PrivateBank'),
    SmallFinanceBank('SmallFinanceBank')
]

banks_working_hours(banks_new)

"""
RBI now has a virtual method working_hours. We have each banks extend the RBI class and implement the virtual working_hours method.
Every class adds its own implementation on how it suites to client friendly and employee friendly working hours. 
The working_hours iterates through the array of banks and just calls its working_hours method.
Now, if we add a new Banks, banks_working_hours doesn’t need to change. 
All we need to do is add the new Bank to the banks array.
banks_working_hours now conforms to the OCP principle.
"""
