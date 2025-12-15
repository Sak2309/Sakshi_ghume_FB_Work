class Product:

    def __init__(self,p_id=1,p_name='fan',price=50000,quntity=2):

        self.p_id=p_id
        self.p_name=p_name
        self.price=price
        self.quntity=quntity
    
    def __del__(self):
        print("DISTRUCTOR CALLED......")
    
    def showProduct(self):

        print("PRODUCT ID : ",self.p_id)
        print("PRODUCT NAME : ",self.p_name)
        print("PRODUCT PRICE : ",self.price)
        print("PRODUCT QUNTITY: ",self.quntity)

print("Parameterized....")
p1 = Product(102,'washing machian',56000,3)
p1.showProduct()

print("parameterless.....")
p2 = Product()
p2.showProduct()
    