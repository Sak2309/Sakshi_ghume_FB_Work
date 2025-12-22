class Person:
    def __init__(self,name,address,balance):
        self.name=name #public
        self._address=address #protected
        self.__balance=balance
    
p1 = Person('sakshi','pune',1000000)
print(p1.name)
print(p1._address)
print(p1.__balance)