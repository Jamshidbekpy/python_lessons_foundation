from main_abc import ProductStructure
from datetime import datetime

class Product(ProductStructure):
    
    __date_of_arrival = datetime.now()
    @classmethod
    def get_department_and_name(cls):
        l_department = ['','Ichimliklar','Oziq-ovqat']
        for index,department in enumerate(l_department):
            if index == 0:
                continue
            print(f'{index} --> {department}')
        select = input('Bolimni tanlang/0: ')
        if select.isdigit() and int(select) > 0 and int(select) < len(l_department):
            select = l_department[int(select)]
            select_name = input('Mahsulot nomini kiriting:')
            return [select,select_name]
        elif select == '0':
            return 0        
        else :
            print('Bo\'lim nomi xato kiritildi!Iltimos boshqatdan kiriting!')
            return 0
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
                return date
            except:
                print('Chiqarilgan sana xato kiritildi!') 
    @classmethod
    def get_expiration_date(cls):
        while True:
            expiration_date = input('Muddati tugaydigan sanani kiriting *kun/oy/yil*:')
            try:  
                date = datetime.strptime(expiration_date,'%d/%m/%Y')
                return date
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
    
    
        
    
