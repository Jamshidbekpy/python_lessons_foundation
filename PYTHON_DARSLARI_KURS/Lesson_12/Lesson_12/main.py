from shop import Shop

def shop_create():
    name = input('Do\'kon nomini kiriting:')
    if name == '0':
        exit()
    location = input('Joylashuvni kiriting:')
    data = f'{name}.xlsx'
    
    return name,location,data

while True:
    info = shop_create()
    shop = Shop(*info)
    shop.main()
    
        
        
   

