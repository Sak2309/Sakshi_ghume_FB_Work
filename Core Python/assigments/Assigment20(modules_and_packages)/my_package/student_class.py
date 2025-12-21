from sy import Symarks
from ty import Tymarks

class Student :

    def __init__(self,roll_no,name,sy_marks,ty_marks):
        self.roll_no = roll_no
        self.name = name
        self.sy_marks=sy_marks
        self.ty_marks=ty_marks

    def calculate(self):
        total = self.sy_marks.computer + self.ty_marks.computer
        percentage = total / 2

        if (percentage >= 80):
            grade = 'A'
        elif(percentage >= 60):
            grade = 'B'
        elif(percentage >= 50):
            grade = 'C'
        elif(percentage >= 40):
            grade = 'pass'
        else:
            grade = 'Fail'
        return total,percentage,grade
    
    def display(self):
        total,percentage,grade = self.calculate()
    
        print("roll number : ",self.roll_no)
        print("name : ",self.name)
        print("sy computer : ",self.sy_marks)
        print("ty computer : ",self.ty_marks)
        print("total : ",total)
        print("percentage : ",percentage)
        print("grade : ",grade)


        