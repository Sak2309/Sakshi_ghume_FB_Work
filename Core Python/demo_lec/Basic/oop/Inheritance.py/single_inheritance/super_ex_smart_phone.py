#inheritance reuseabilty of code

class Device: #base class
    def __init__(self,brand,model,color,price):
        self.brand=brand
        self.model=model
        self.color=color
        self.price=price

    def getData(self):
        print("BRAND : ",self.brand)
        print("MODEL : ",self.model)
        print("COLOR : ",self.color)
        print("PRICE : ",self.price)

class Smart_phone(Device):
    def __init__(self,b,m,c,p,camera):
        super().__init__(b,m,c,p)
        self.camera=camera

    def getData(self):
        super().getData()
        print("CAMERA : ",self.camera)

d1 = Smart_phone('onepulse','nord 13 R','black',30000,'30 pxl')
d1.getData()