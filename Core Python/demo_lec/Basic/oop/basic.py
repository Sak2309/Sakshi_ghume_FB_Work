#class name ex :Emp 1st letter should be capital
#self :
#1.refernce of current invoking object
#2.to access the value of attribute of object
#3.to associate value with attribute
class Emp:
    def setData(self,id,name,sal,dept):
        
        self.eid=id
        self.ename=name
        self.esalary=sal
        self.edept=dept

    def getData(self):
        
        print("ID : ",self.eid)
        print("NAME : ",self.ename)
        print("SALARY : ",self.esalary)
        print("DEPARTMENT : ",self.edept)
        
obj = Emp()
obj.setData('101','sakshi',34000,'data science')
obj.getData()