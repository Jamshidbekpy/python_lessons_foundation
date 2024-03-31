class Person:
    def __init__(self, name, age, gender, address, phone_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone_number = phone_number
        
    def get_phone_number(self):  # Funksiyani phone_number o'rniga get_phone_number deb nomlang
        return self.phone_number  # Va telefon raqamini qaytaradi

class Student(Person):  # Person klassidan meros olamiz
    def __init__(self, name, gender, address, student_id):  
        super().__init__(name, gender, address, None,age = None)  # Parent klassning __init__ metodini chaqiramiz va phone_number ni None sifatida uzatamiz
        self.student_id = student_id  # Student ID ni qo'shamiz

objP = Person('John', 25, 'Male', '123 Main Street', 151654654658)
objS = Student('Jane', 20, 'Female', '456 Oak Street', 12345)

print(objP.get_phone_number())  # John obyektining telefon raqamini chiqaramiz
print(objS.name)  # Jane obyektining ismini chiqaramiz

