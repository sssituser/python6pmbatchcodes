class Product:
    def __init__(self,pid:int,pname:str,price:int):
        self.pid = pid
        self.pname = pname
        self.price = price
       
    def getproduct(self):
        print(f'Product Id : {self.pid}')
        print(f'Product Name : {self.pname}')
        print(f'Produt Price : {self.price}')
p1 = Product(123,"Dove",75)
p1.getproduct()
        
    