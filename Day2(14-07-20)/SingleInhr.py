#Single level Inheritance
class ClassA:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def show():
        return 'I am from ClassA'
    def add(self):
        return self.a+self.b

class ClassB(ClassA):
    c=25
    a=10
    b=20
    def display():
        return 'I am from ClassB'
    def sub(a,b):
        return a-b
