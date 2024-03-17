
class Circle:
    __radius = None # Private class variable

    def __init__(self,radius) -> None:
        self.__radius = radius
        # Encapsulation

    def getRadius(self):
        return self.__radius 

    def setRadius(self,radius):
        self.__radius = radius   

        
# print(circle.getRadius())
circle = Circle(5.65)

# circle.__radius = 10.504 - Not working! how do I change the value than?
circle.setRadius(10.504)
print(circle.getRadius())
