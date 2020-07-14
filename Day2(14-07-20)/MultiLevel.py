#Multilevel
class A:
    def ClassA():
        return "i am from ClassA"

class B(A):
    def ClassB():
        return 'i am from ClassB'

class C(B):
    def ClassC():
        return 'i am from ClassC'
