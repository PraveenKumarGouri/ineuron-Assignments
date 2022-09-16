class bank:
    def transaction(self):
        print("total transaction value")
    def account_opening(self):
        print("this will show your account opening status")
    def deposite(self):
        print("this will show your deposited amount")
    def test(self):
        print("this is the test method from bank")
class HDFC_bank:
    def hdfc_to_icici(self):
        print("this will show you all the transaction happend to icicic through hdfc")
    def test(self):
        print("this is a test method from hdfc bank")
class ineuron_bank:
    def account_status_icici(self):
        print("print account status in icici")
class icici(HDFC_bank,bank,ineuron_bank):
    pass
i=icici()
i.hdfc_to_icici()
i.deposite()
i.account_opening()
i.transaction()
i.test()
i.account_status_icici()