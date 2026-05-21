# @property: Pythonic way to use getters/setters
# Access private attributes like regular attributes

class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self.__celsius = value

    @property
    def fahrenheit(self):
        return self.__celsius * 9/5 + 32

t = Temperature(25)
print(t.celsius)       # 25
print(t.fahrenheit)    # 77.0

t.celsius = 100
print(t.fahrenheit)    # 212.0
