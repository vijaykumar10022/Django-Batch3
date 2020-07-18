#Single level Inheritance

'''global a
a=10
global b
b=20

class ClassA:
    
    
    def show():
        print(a)
        return 'I am from ClassA'
    def add():
        return a+b'''

class ClassA:
    def __init__(s,a,b):
        s.a=a
        s.b=b
    def show(s):
        return s.a

