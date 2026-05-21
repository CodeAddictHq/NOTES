# Simple OOP template with generic names

class ClassName():
    # class attribute
    clsAttribute = 0

    # constructor defines what properties every object will have
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.anotherAttribute = "static defined val"
        ClassName.clsAttribute += 1
 
    # method is function of objects and self indicates the object itself (does oparetion in the calling obj)
    def methodName(self):
        print("Name:", self.name)
        print("Value:", self.value)

    # cls indicates the class itself 
    @classmethod
    def clsMethod(cls):
        print("Total objects:", cls.clsAttribute)


# objects creation
Object1 = ClassName("A", 10)
Object2 = ClassName("B", 20)
Object3 = ClassName("C", 30)
 
 

#object property access obj.property
object1.value
#Class property access obj.property
ClassName.clsAttribute
Object1.clsAttribute #can be accessed via this though


# method calls
Object1.methodName()

# class method call
ClassName.clsMethod()