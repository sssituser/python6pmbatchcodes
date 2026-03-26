class Test:
    def readvalues(self,a,b):
        self.a = a
        self.b = b
    def showvalues(self):
        print(f'a = {self.a}\t b = {self.b}')
class Opeations(Test):
    def sum(self):
        print(f'sum a and b is :{self.a+self.b}')
    def sub(self):
        print(f'Sub of  a and b is {self.a-self.b}')
        
op = Opeations()
op.readvalues(5,2)
op.showvalues()
op.sum()
op.sub()