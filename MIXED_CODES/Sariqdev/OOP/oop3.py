class Person:
    def __init__(self, first_name, last_name, year_of_birth, passport_series):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.pasport_series = passport_series
        self.age = 0
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_year_of_birth(self):
        return self.year_of_birth
    def get_passport_series(self):
        return self.pasport_series
    def set_age(self):
        self.age = int(input("Current year:"))-self.year_of_birth
    def get_age(self):
        self.set_age()
        return self.age

    def get_info(self):
        return f"""
First name:{self.get_first_name()}
Last name: {self.get_last_name()}
Year of birth:{self.get_year_of_birth()}
Passport series:{self.get_passport_series()}
Age:{self.get_age()} years old
"""

new_person = Person(first_name = "Jahongir",last_name = "Farmonqul", year_of_birth = 1970,passport_series = "AC0697717")
# print(new_person.get_age())
# print(new_person.get_info())




class Scienses:
    n = 0
    name_list = []
    def set_name_list(self):
        if self.n == 0:
            print("Enter 1 of the subjects you know. Then enter 0")
        name = input("New sciense:")
        if name != "0":
            self.name_list.append(name)
            self.n += 1
            self.set_name_list()
    def get_name_list(self):
        self.set_name_list()
        return self.name_list

new_scienses = Scienses()
# print(new_scienses.get_name_list())




class Student(Person):
    n = 0
    def __init__(self,first_name, last_name, year_of_birth, passport_series, university_name, address):
        #Voris olish
        super().__init__(first_name, last_name, year_of_birth, passport_series)
        self.university_name = university_name
        self.address = address
        self.sciences = []
        self.cours = 0
    def get_university_name(self):
        return self.university_name
    def get_address(self):
        return self.address
    def set_sciences(self):
        self.sciences = new_scienses.get_name_list()
    def get_science(self):
        self.set_sciences()
        return self.sciences

    def set_cours(self):
        self.cours = self.get_age() - 18
    def get_cours(self):
        self.set_cours()
        return self.cours
    #Polimorfizm
    def get_info(self):
        return f"""
First name:{self.get_first_name()}
Last name: {self.get_last_name()}
Year of birth:{self.get_year_of_birth()}
Passport series:{self.get_passport_series()}
Age:{self.get_age()} years old
University name:{self.get_university_name()}
Address:{self.get_address()}
Stage:{self.get_cours()}
Sciences:{self.get_science()}
"""

new_student = Student(first_name = "Jamshidbek", last_name = "Shodibek", year_of_birth = 2004, passport_series = "AD0897717",university_name = "TUIT",address = "TTJ-2")
# print(new_student.get_science())
print(new_student.get_info())

