class A:
    def ClassA():
        return "i am from ClassA"

class B:
    def ClassB():
        return 'i am from ClassB'

class C(A,B):
    def ClassC():
        return 'i am from ClassC'
