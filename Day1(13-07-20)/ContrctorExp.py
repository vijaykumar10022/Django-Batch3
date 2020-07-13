class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def display(self):
        return {'name':self.name,'roll':self.roll}
