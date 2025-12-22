#static variable:

#1.class level variable
#2.only one copy is created
#3.how access the static variable: class name.static variables 

#non static varibles :

#1.obj level variables
#2.no of object copies created.
#3.used object  name to access such variables

class Account:

    branch = 'SBI' #static varible

    def __init__(self,holder_name,acc_no,balance):
        self.holder_name=holder_name
        self.acc_no=acc_no
        self.balance=balance
    
    def getData(self):

        data = "BRANCH NAME : "+ Account.branch
        data += "HOLDER NAME : "+ self.holder_name
        data += "\nACCOUNT NO : "+ str(self.acc_no)
        data += "\nBALANCE : "+ str(self.balance)
        return data
    
ac = Account("sakshi",123456789,45000)
print(ac.getData())
print(Account.branch) #accesss the static variable 