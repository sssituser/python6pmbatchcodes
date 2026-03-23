class Product:
    def set_Product(self,pro_id,pro_name,pro_price):
        self.pro_id =pro_id
        self.pro_name = pro_name
        self.pro_price = pro_price
    def showProduct(self):
        print(f'Product id :{self.pro_id}')
        print(f'Product Name :{self.pro_name}')
        print(f'Product Price :{self.pro_price}')
        
        
p1 = Product()
p1.set_Product(111,"abc",400)    
p1.showProduct()    
        