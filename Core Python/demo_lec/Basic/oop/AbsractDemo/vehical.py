from abc import ABC , abstractmethod

class Vechical(ABC):

    @abstractmethod
    def speed():
        pass

class Bike(Vechical):

    def __init__(self,model,price):

        self.model=model
        self.price=price

    def speed(self):

        print("MODEL NAME : ",self.model)
        print("PRICE : ",self.price)

class Car(Vechical):

    def __init__(self,model,price):

        self.model=model
        self.price=price

    def speed(self):
        
        print("MODEL NAME : ",self.model)
        print("PRICE : ",self.price)

class scooti(Vechical):

    def __init__(self,model,price):

        self.model=model
        self.price=price

    def speed(self):
        
        print("MODEL NAME : ",self.model)
        print("PRICE : ",self.price)

b = Bike('hero',40000)
c = Car('hundai',700000)
s = scooti('activa',60000)

li_of_object= [b,c,s]
for obj in li_of_object:
    obj.speed()

        
