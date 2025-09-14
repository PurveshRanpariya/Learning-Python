class Animals:
    pass 

class Pets(Animals):
    pass 

class Dog(Pets):
    def __init__(self,name,d):
        self.name=name
        self.d=d
    
    def bark(self):
        print(f"dog name is {self.name} , sound is {self.d}")

d=Dog("tommy","bow bow")
d.bark()        
        

        
    
    

    


