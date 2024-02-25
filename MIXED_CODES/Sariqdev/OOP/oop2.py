class Avto:
    def __init__(self, model, color, karobka, price):
        self.model = model
        self.color = color
        self.karobka = karobka
        self.price = price
        self.kilometr = 0
    def get_model(self):
        return self.model
    def get_color(self):
        return self.color
    def get_karobka(self):
        return self.karobka
    def get_price(self):
        return self.price
    def update_km(self,update_km):
        self.kilometr += update_km
    def get_kilometr(self):
        self.update_km(2)
        return self.kilometr
    def get_info(self):
        return f"This is {self.get_model()}'s color {self.get_color()},karobka {self.get_karobka()},price {self.get_price()} and this is the path of the car {self.get_kilometr()}"

new_Car = Avto(model = 'Mersedes',color = 'Green',karobka = 'Avtomat',price = 12000)
class Avtosalon:
    def __init__(self, name, address, cars_for_sale, cars):
        self.name = name
        self.address = address
        self.cars_for_sale = cars_for_sale
        self.cars = cars
    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
    def get_cars_for_sale(self):
        return self.cars_for_sale
    def get_cars(self):
        return self.cars
    def add_car(self):
        car = new_Car.get_model()
        self.cars.append(car)
    def get_now_cars(self):
        self.add_car()
        return self.cars
    def get_info(self):
        return f""" 
Our new Avtosolon {self.get_name()}.It's in Tashkent.
Exact address {self.get_address()}.
Our have {self.get_cars()} named cars in Avtosalon.
Recently, another model of car has been added to us.
Our current list of cars:{self.get_now_cars()}
"""

new_Avtosalon = Avtosalon(name = 'Bright',address = 'Chilonzor',cars_for_sale = ['Tico','Nexia','Lasetti','Damas'],cars = ['Tico','Nexia','Lasetti','Damas','Matiz','Spark'])
print(new_Avtosalon.get_info())
print(dir(Avto),'\n',dir(Avtosalon))
print(Avtosalon.__dict__.keys())
print(new_Avtosalon.__dict__.keys())