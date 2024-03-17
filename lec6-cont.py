class Person:
    # Protected - Access modifier 
    _name = None
    _age = None
    _designation = None

    def __init__(self,name,age,designation) -> None:
        self._name = name
        self._age = age
        self._designation = designation

person = Person("Huzaifa",22,"Backend Engineer")

print(person._name) # Error - you cannot access it directly