class A:
    def getValues(self):
        self.a = int(input('Enter a value : '))
        self.b = int(input('Enter b value : '))
    def showValues(self):
        print(f'a = {self.a}\tb = {self.b}')

class B(A):# line is for inheritance      
    def mul(self):
        print(f'mul of a an b is : {self.a*self.b}')
    def div(self):
        print(f'Quo is :{self.a/self.b}')
        
class C(B):
    def sum(self):
        print(f'Sum of a and b is : {self.a+self.b}')
    def sub(self):
        print(f'Sub of a and b is : {self.a-self.b}')
c = C()
c.getValues()
c.showValues()
c.sum()
c.sub()
c.mul()
c.div()
        

        
        

