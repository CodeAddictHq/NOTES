# by inheriting another class we can use another classes property and methods in child class

class ParentClass:
    #methods attributes....
                #heres hpw we inherit
class ChildClass(ParentClass):
  #no degined thing
# object
childClassObject = ChildClass()


#as we have inherited parent we can use
"""
Class attributes
Methods
Constructor (__init__)
"""


#1. Class attributes
ChildClass.ParentClassAttribute
childClassObject.ParentClassAttribute 

#2. Methods
ChildClass.ParentClassMethod()
childClassObject.ParentClassMethod() 

#3. Constructor - A constructor is a special routine that automatically executes when an object is created
"""
class ParentClass:
    def __init__(self, name):
        self.name = name
        print("Parent:", self.name)
class ChildClass(ParentClass):
    def __init__(self, name, age):
        super().__init__(name)# pass argument to parent
        self.age = age
        print("Age:", self.age)
Object = ChildClass("Adib", 17)
"""