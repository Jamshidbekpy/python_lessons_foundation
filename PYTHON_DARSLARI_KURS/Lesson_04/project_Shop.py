from colorama import init, Fore
init(autoreset=True)
# """
#                                            Database bo'limi
# """
database = {
    "Drinks (piece)": {
        "Kola": 142, "Pepsi": 154, "Fanta": 145, "Sayhun": 214, "Smile": 124
    },
    "Vegetables (kg)": {
        "Carrot": 1548.6, "Potatoes": 2156.2, "Onion": 1254.4, "Eggplant": 125
    },
    "Cereal-products (kg)": {
        "Rice": 4587, "Wheat": 3254.4, "Peas": 968, "Mosh": 658, "Bean": 859.2, "Corn": 1454
    },
    "Fruits (kg)": {
        "Banana": 125, "Apple": 457.7, "Apelsin": 786, "Apricot": 456
    },
    "Snacks (piece)": {
        "Chips": 300, "Chocolate": 500, "Candy": 700
    },
    "Dairy-products (kg)": {
        "Milk": 2000, "Cheese": 300, "Yogurt": 500
    },
    "Bakery-products (piece)": {
        "Bread": 200, "Croissant": 150, "Bagel": 100
    },
    "Meat (kg)": {
        "Beef": 500, "Chicken": 800, "Pork": 300
    },
    "Frozen-food (kg)": {
        "Fish": 400, "Shrimp": 600, "Pizza": 200
    },
    "Condiments (piece)": {
        "Salt": 500, "Pepper": 300, "Ketchup": 400
    },
    "Cleaning-products (piece)": {
        "Soap": 200, "Detergent": 300, "Bleach": 150
    }
}

# """
#                                           Add_Product bo'limi
# """
database_r = {}
database_s = {}
for key, value in database.items():
    database_r[key] = value.copy()
    for key_2, value_2 in database_r[key].items():
        database_r[key][key_2] = 0

for key, value in database.items():
    database_s[key] = value.copy()
    for key_2, value_2 in database_s[key].items():
        database_s[key][key_2] = 0
# """
#                              Mavjud mahsulotlarni ko'rish bo'limi
# """
for key, value in database.items():
    print(Fore.BLUE + 135 * "-")
    print(Fore.BLUE + key.center(135))
    print(Fore.GREEN+135*"-")
    for key_2, value_2 in value.items():
        print(Fore.GREEN + key_2, end="   ")
    print()

print(Fore.LIGHTRED_EX + "Iltimos,kiritayotgan mahsulotingizning nomini to'liq va aniq kiriting!\n".center(135))
while True:
    add_or_sold = input(Fore.RED + "Mahsulot qo'shmoqchimisiz,sotmoqchimisiz,report bo'limi,database va hisobni tugatish: +/-/?/DB/0:")
    if add_or_sold == "+":
        while True:
            add_product_key = input(Fore.CYAN + "Add product (Oilasi) /0:")
            if add_product_key != "0":
                database_r_key = add_product_key
                database_s_key = add_product_key
                if not (add_product_key in database):
                    add_product_value = {}
                    database_r_value = {}
                    database_s_value = {}
                    while True:
                        add_product_value_key = input(Fore.LIGHTGREEN_EX + "Add product name (nomi) /0:")
                        if add_product_value_key != "0":
                            database_r_value_key = add_product_value_key
                            if not (add_product_value_key in add_product_value):
                                database_s_value_key = add_product_value_key
                                while True:
                                    add_product_value_value = input(Fore.LIGHTRED_EX + "Add_Miqdori:")
                                    if add_product_value_value.isdigit() and int(add_product_value_value) >= 0:
                                        add_product_value_value = int(add_product_value_value)
                                        database_r_value_value = add_product_value_value
                                        database_s_value_value = 0
                                        add_product_value[add_product_value_key] = add_product_value_value
                                        database_r_value[database_r_value_key] = database_r_value_value
                                        database_s_value[database_s_value_key] = database_s_value_value
                                        break
                                    else:
                                        print(Fore.LIGHTRED_EX + "Musbat qiymat kiritmadingiz,yoki sonni kiritishda xatolikka yo'l qo'ydingiz!".center(135))
                            else:
                                while True:
                                    add_product_value_value = input(Fore.LIGHTRED_EX + "Add_Miqdori:")
                                    if add_product_value_value.isdigit() and int(add_product_value_value):
                                        database_r_value_value = add_product_value_value
                                        add_product_value[add_product_value_key] += add_product_value_value
                                        database_r_value[add_product_value_key] += add_product_value_value
                                        break
                                    else:
                                        print(Fore.LIGHTRED_EX + "Musbat qiymat kiritmadingiz,yoki sonni kiritishda xatolikka yo'l qo'ydingiz!".center(135))
                        else:
                            break
                    database[add_product_key] = add_product_value
                    database_r[database_r_key] = database_r_value
                    database_s[database_s_key] = database_s_value
                else:
                    add_product_value_key = input(Fore.LIGHTGREEN_EX + "Add product name (nomi) /0:")
                    if add_product_value_key != "0":
                        database_r_value_key = add_product_value_key
                        if not (add_product_value_key in database[add_product_key]):
                            database_s_value_key = add_product_value_key

                            while True:
                                add_product_value_value = input(Fore.LIGHTRED_EX + "Add_Miqdori:")
                                if add_product_value_value.isdigit() and int(add_product_value_value) >= 0:
                                    add_product_value_value = int(add_product_value_value)
                                    database_r_value_value = add_product_value_value
                                    database_s_value_value = 0
                                    database[add_product_key][add_product_value_key] = add_product_value_value
                                    database_r[database_r_key][database_r_value_key] = database_r_value_value
                                    database_s[database_s_key][database_s_value_key] = database_s_value_value
                                    break
                                else:
                                    print(Fore.LIGHTRED_EX + "Musbat qiymat kiritmadingiz,yoki sonni kiritishda xatolikka yo'l qo'ydingiz!".center(135))
                        else:
                            while True:
                                add_product_value_value = input(Fore.LIGHTRED_EX + "Add_Midori:")
                                if add_product_value_value.isdigit() and int(add_product_value_value) >= 0:
                                    add_product_value_value = int(add_product_value_value)
                                    database_r_value_value = add_product_value_value
                                    database[add_product_key][add_product_value_key] += add_product_value_value
                                    database_r[database_r_key][database_r_value_key] += database_r_value_value
                                    break
                                else:
                                    print(Fore.LIGHTRED_EX + "Musbat qiymat kiritmadingiz,yoki sonni kiritishda xatolikka yo'l qo'ydingiz!".center(135))

            else:
                break
# """
#                                           Sold Product bo'limi
# """
    elif add_or_sold == "-":
        while True:
            sold_product_key = input(Fore.CYAN + "Sold product (Oilasi) /0:")
            if sold_product_key != "0":
                # database_s_key = sold_product_key
                if not(sold_product_key in database):
                    print(Fore.LIGHTBLUE_EX + "Bizda bunday mahsulot yo'q edi!Istasangiz buyurma qilishingiz mumkin!".center(135))
                    #Buyurtma bo'limiga yuboriladi
                else:
                    database_s_key = sold_product_key
                    sold_product_value = database[sold_product_key]
                    sold_product_value_key = input(Fore.LIGHTGREEN_EX + "Sold product name (nomi) /n:")
                    if not(sold_product_value_key in sold_product_value):
                        print(Fore.LIGHTBLUE_EX + "Bizda bunday mahsulot yo'q edi!Istasangiz buyurma qilishingiz mumkin!".center(135))
                        # Buyurtma bo'limiga yuboriladi
                    else:
                        database_s_value = database_s[database_s_key]
                        database_s_value_key = sold_product_value_key
                        while True:
                            sold_product_value_value = input(Fore.LIGHTRED_EX + "Sold_Miqdori:")
                            if sold_product_value_value.isdigit() and int(sold_product_value_value) >= 0:
                                sold_product_value_value = int(sold_product_value_value)
                                database_s_value_value = sold_product_value_value
                                if database[sold_product_key][sold_product_value_key] >= sold_product_value_value:
                                    database[sold_product_key][sold_product_value_key] -= sold_product_value_value
                                    database_s[database_s_key][database_s_value_key] += database_s_value_value
                                    break
                                else:
                                    database_s[database_s_key][database_s_value_key] += 0
                                    print(Fore.LIGHTBLUE_EX + f"Kechirasiz bizda ushbu mahsulot sizga kerakli miqdordan {sold_product_value_value - database[sold_product_key][sold_product_value_key]} kam!Hohlasangiz kamroq oling.Olmasangiz 0 ni kiriting!".center(135))
                            else:
                                print(Fore.LIGHTRED_EX + "Musbat qiymat kiritmadingiz,yoki sonni kiritishda xatolikka yo'l qo'ydingiz!".center(135))

            else:
                break
# """
#                                                 Report bo'limi
# """
    elif add_or_sold == "?":
        print(Fore.LIGHTRED_EX + "Ushbu mahsulotlar sotildi:".center(135))
        print()
        for key, value in database_s.items():
            print(Fore.BLUE + 135 * "-")
            print(Fore.BLUE + key.center(135))
            print(Fore.GREEN + 135 * "-")
            for key_2, value_2 in value.items():
                print(Fore.LIGHTMAGENTA_EX + key_2 + "==>", Fore.LIGHTMAGENTA_EX + str(value_2), end="   ")
            print()
        print(Fore.LIGHTRED_EX + "Ushbu mahsulotlar yangi keldi:".center(135))
        print()
        for key, value in database_r.items():
            print(Fore.BLUE + 135 * "-")
            print(Fore.GREEN + key.center(135))
            print(Fore.GREEN + 135 * "-")
            for key_2, value_2 in value.items():
                print(Fore.LIGHTYELLOW_EX + key_2 + "==>", Fore.LIGHTMAGENTA_EX + str(value_2), end="   ")
            print()
    elif add_or_sold == "DB":
        print(Fore.RED + "Ogohlantirish:Ushbu bolimga kirish cheklangan!")
        login = input(Fore.CYAN + "Loginni kiriting:")
        password = input(Fore.CYAN + "Passwordni kiriting:")
        if login == "Jamshidbek" and password == "11.06.2004":
            print(Fore.LIGHTRED_EX + "Ba'zadagi mahsulotlar:".center(135))
            print()
            for key, value in database.items():
                print(Fore.BLUE + 135 * "-")
                print(Fore.LIGHTMAGENTA_EX + key.center(135))
                print(Fore.GREEN + 135 * "-")
                for key_2, value_2 in value.items():
                    print(Fore.LIGHTBLUE_EX + key_2 + "==>", Fore.LIGHTRED_EX + str(value_2), end="   ")
                print()
        else:
            print(Fore.LIGHTRED_EX + "Siz uchun bu bo'limga ruxsat yo'q!")
    elif add_or_sold == "0":
        break

# """
#                                                Buyurtma bo'limi
# """


