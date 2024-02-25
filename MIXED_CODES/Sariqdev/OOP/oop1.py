class User:
    def __init__(self,client_name, client_surname, email,client_age):
        self.client_name=client_name
        self.client_surname=client_surname
        self.email=email
        self.client_age=client_age
    def get_info(self):
        return f'{self.client_name} {self.client_surname} {self.client_age} yoshda.Emaili {self.email}'
name = input("Client name:")
surname = input("Client surname:")
email = input("Client email:")
age = input("Client age:")
new_object1=User(name,surname,email,age)
print(new_object1.get_info())
print(new_object1.client_name)
print(new_object1.client_surname)
print(new_object1.email)
print(new_object1.client_age)