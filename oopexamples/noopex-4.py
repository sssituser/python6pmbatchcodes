class Product:
    def setProudct(self,pid,pname,price):
        self.pid= pid
        self.pname = pname
        self.price = price
        
p1  = Product() # creation object
p1.setProudct(123,"vivo",500)
print(p1.pid,p1.pname,p1.price)
        