#assign 4
#  Class Variables and Class Methods

class Bank:
    bank_name = "National Bank"       # Class variable

    @classmethod
    def change_bank_name(cls, name):  # Class method
        cls.bank_name = name

b1 = Bank()
b2 = Bank()
print(Bank.bank_name)
Bank.change_bank_name("Global Bank") # Change class variable
print(b1.bank_name, b2.bank_name)    # Reflects in all instances
# Explanation:
#	Changing bank_name affects all instances because it’s shared.
