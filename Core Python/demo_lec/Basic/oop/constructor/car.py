class Car:
    def __init__(self,brand,color,price):
        self.brand = brand
        self.color=color
        self.price=price
    
    def getData(self):
        data = 'BRAND : '+self.brand+'\n'
        data += 'COLOR :'+self.color+'\n'
        data += 'PRICE :'+str(self.price)+'\n'
        return data

c1= Car('bmw','black',100000000)
c2= Car('honda','black',250000)

print(c1.getData())
print(c2.getData())