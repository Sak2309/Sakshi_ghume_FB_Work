class Cricketor:
    def __init__(self,name,age,role):
        self.name=name
        self.age=age
        self.role=role
    
    def getData(self):
        print("NAME:",self.name)
        print("AGE:",self.age)
        print("ROLE:",self.role)
    
    def __del__(self):
        print("Distructor called")

c1=Cricketor('sachian',55,'batsman')
del c1
c1.getData()
