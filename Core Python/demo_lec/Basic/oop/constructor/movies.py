#default and parameterized constructor
class Movie:
    def __init__(self,name ='yjhd',gener ='drama',dict='ayaan'):#defult
        self.name=name
        self.gener=gener
        self.dicreator=dict

    def getData(self):
        data = f'Name :{self.name}\nGener:{self.gener}\ndirector:{self.dicreator}'
        return data

m1 = Movie()
m2 =Movie('kkkg','romance','karan')#parameterized

print(m1.getData())
print(m2.getData())
        