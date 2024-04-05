from main_abc import ProductStructure
from datetime import datetime

class Product(ProductStructure):
    
    __date_of_arrival = datetime.now()
    @classmethod
    def get_quantity(cls):
        while True:
            quantity = input('Miqdorni kiriting:')
            if quantity.isdigit() and int(quantity) > 0:
                return int(quantity)
            else:
                print('Miqdor xato kiritildi!')
    @classmethod
    def get_price(cls):
        while True:
            price = input('Narxni kiriting:')
            if price.isdigit() and int(price) > 0:
                return int(price)
            else:
                print('Miqdor xato kiritildi!')
    @classmethod
    def get_old_date(cls):
        while True:
            old_date = input('Chiqarilgan sana kiriting *kun/oy/yil*:')
            try:  
                date = datetime.strptime(old_date,'%d/%m/%Y')
                if date < cls.__date_of_arrival:
                    return date
                else:
                    print('Chiqarilgan sana xato kiritildi!')
            except:
                print('Chiqarilgan sana xato kiritildi!') 
    @classmethod
    def get_expiration_date(cls):
        while True:
            expiration_date = input('Muddati tugaydigan sanani kiriting *kun/oy/yil*:')
            try:
                date = datetime.strptime(expiration_date,'%d/%m/%Y')
                if date > cls.__date_of_arrival:
                    return date
                else:
                    print('Muddati tugaydigan sana xato kiritildi!')
            except:
                print('Muddati tugaydigan sana xato kiritildi!') 
        pass
    @classmethod
    def get_date_of_arrival(cls):
        return cls.__date_of_arrival
    @classmethod
    def get_country(cls):
        select = input('Davlat nomini kiriting:')
        return select
    
    
        
    
