class Product:
    def setProduct(self,pid,pname,pprice):
        self.pid = pid
        self.pname = pname
        self.pprice = pprice
    def getproduct(self):
        print(f'Produt ID : {self.pid}')
        print(f'Produt Name : {self.pname}')
        print(f'Product Price : {self.pprice}')
p1 = Product() # p1 object created 
p1.setProduct(123,"Soap : Dove",65)
p1.getproduct()

p2 = Product()
p2.setProduct(144,"RIN Washing Powder",500)
p2.getproduct()
        