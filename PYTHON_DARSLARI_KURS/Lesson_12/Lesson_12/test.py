class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old"
    def obj(self):
        obj1 = Person("John", 36)
        print(obj1.get_info())
        return self.get_info()
obj2 = Person("Jamshidbek", 36)

print(obj2.get_info())
print(obj2.obj())


