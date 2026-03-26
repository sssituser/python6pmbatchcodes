class A:
    def readvalues(self):
        self.a = int(input('Enter a value : '))
        self.b = int(input('Enter b value : '))
    def showvalues(self):
        print(f' a = {self.a}\tb = {self.b}')
    
class B(A):
    def sum(self):
        print(f'sum of  and b is {self.a+self.b}')
    
    
class C:
    def squre(self,num):
        print(f'Square is :{num*num}')
    
class D(B,C):
    def sub(self):
        print(f'sub of  a and b values is {self.a-self.b}')
d = D()

d.readvalues()
d.showvalues()
d.sum()
d.sub()
