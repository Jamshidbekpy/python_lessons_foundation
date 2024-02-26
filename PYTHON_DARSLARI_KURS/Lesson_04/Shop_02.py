from colorama import init, Fore
init(autoreset=True)
#  __________________________________________________________DATABASE_________________________________________________________
database = {
    "Sabzavotlar (kg)": [["Karam", "Piyoz"], [150, 250]],
    "Mevalar (kg)": [["Shaftoli", "Nar", "Anor"], [365, 210, 150]],
    "Ichimliklar (dona)": [["Pepsi", "Sprite"], [300, 200]],
    "Sut (l)": [["Tuxum", "Qatiq"], [10, 20]],
    "Yog' (kg)": [["Qatiqli"], [50]]
}
add_database = {}
sold_database = {}
for key, value in database.items():
    value_0 = value[0]
    value_1 = value[1].copy()
    value_01 = value[0]
    value_11 = value[1].copy()
    add_database[key] = [value_0, value_1]
    sold_database[key] = [value_01, value_11]
for key, value in add_database.items():
    for i in range(len(value[1])):
        value[1][i] = 0
for key, value in sold_database.items():
    for i in range(len(value[1])):
        value[1][i] = 0
while True:
    bolim = input("Qoshish, sotish, report yoki database bo'limi tanlang (1/2/3/4), 0-chiqish: ")
#    _______________________________YANGI MAHSULOTLARNI QABUL QILISH BO'LIMI____________________________________________________
    if bolim == "1":
        while True:
            add_database_key = input("Oila nomini kiriting/0:")
            if add_database_key == "0":
                break
            if add_database_key in add_database:
                add_database_key_list0_element = input("Mahsulot nomini kiriting/0:")
                if add_database_key_list0_element == "0":
                    break
                if add_database_key_list0_element in add_database[add_database_key][0]:
                    index = add_database[add_database_key][0].index(add_database_key_list0_element)
                    while True:
                        add_database_key_list1_element = input("Miqdorini kiriting:")
                        if add_database_key_list1_element.isdigit() and int(add_database_key_list1_element) >= 0:
                            add_database_key_list1_element = int(add_database_key_list1_element)
                            add_database[add_database_key][1][index] += add_database_key_list1_element
                            database[add_database_key][1][index] += add_database_key_list1_element
                            break
                        else:
                            print("Noto'g'ri miqdor kiritildi, iltimos qaytadan urinib ko'ring!")

                else:
                    add_database[add_database_key][0].append(add_database_key_list0_element)
                    while True:
                        add_database_key_list1_element = input("Miqdorini kiriting:")
                        if add_database_key_list1_element.isdigit() and int(add_database_key_list1_element) >= 0:
                            add_database_key_list1_element = int(add_database_key_list1_element)
                            add_database[add_database_key][1].append(add_database_key_list1_element)
                            database[add_database_key][1].append(add_database_key_list1_element)
                            break
                        else:
                            print("Noto'g'ri miqdor kiritildi, iltimos qaytadan urinib ko'ring!")
            else:
                add_database_key_list0_element = input("Mahsulot nomini kiriting/0:")
                if add_database_key_list0_element == "0":
                    break
                add_database.setdefault(add_database_key, [[], []])
                database.setdefault(add_database_key, [[], []])
                add_database[add_database_key][0].append(add_database_key_list0_element)
                database[add_database_key][0].append(add_database_key_list0_element)
                while True:
                    add_database_key_list1_element = input("Miqdorini kiriting:")
                    if add_database_key_list1_element.isdigit() and int(add_database_key_list1_element) >= 0:
                        add_database_key_list1_element = int(add_database_key_list1_element)
                        add_database[add_database_key][1].append(add_database_key_list1_element)
                        database[add_database_key][1].append(add_database_key_list1_element)
                        break
                    else:
                        print("Noto'g'ri miqdor kiritildi, iltimos qaytadan urinib ko'ring!")
#      _________________________________________SOTUV BO'LIMI_________________________________________________
    elif bolim == "2":
        while True:
            sold_database_key = input("Sotiladigan mahsulot oilasini kiriting:")
            if sold_database_key in sold_database:
                while True:
                    sold_database_key_list0_element = input("Sotiladigan mahsulot nomini kiriting/0:")
                    if sold_database_key_list0_element == "0":
                        break
                    if sold_database_key_list0_element in sold_database[sold_database_key][0]:
                        while True:
                            sold_database_key_list1_element = input("Mahsulot miqdorini kiriting:")
                            index = sold_database[sold_database_key][0].index(sold_database_key_list0_element)
                            if sold_database_key_list1_element.isdigit()  and database[sold_database_key][1][index] >= int(sold_database_key_list1_element):
                                sold_database_key_list1_element = int(sold_database_key_list1_element)
                                sold_database[sold_database_key][1][index] += sold_database_key_list1_element
                                database[sold_database_key][1][index] -= sold_database_key_list1_element
                                break
                            else:
                                print("Noto'g'ri miqdor kiritildi, iltimos qaytadan urinib ko'ring!")
                    else:
                        print("Ushbu oilada bunday mahsulot turi yo'q! Iltimos,boshqatdan urinib ko'ring! ")
            else:
                print("Bizda bunday oila turidagi mahsulot yo'q!")
#               ________________________________________REPORT BO'LIMI_______________________________________
    elif bolim == "3":
        print(Fore.LIGHTRED_EX + "Ushbu mahsulotlar yangi keldi:".center(135),"\n")
        for key, value in add_database.items():
            print("\n\n", key)
            for i in range(len(value[0])):
                print(f"{value[0][i]} ==> {value[1][i]}", end="  ")
        print(Fore.LIGHTRED_EX + "Ushbu mahsulotlar sotildi:".center(135),"\n")
        for key, value in sold_database.items():
            print("\n\n", key)
            for i in range(len(value[0])):
                print(f"{value[0][i]} ==> {value[1][i]}", end="  ")
        pass
#               __________________________________DATABASENI KO'RISH BO'LIMI_________________________________
    elif bolim == "4":
        print(Fore.RED + "Ogohlantirish:Ushbu bolimga kirish cheklangan!")
        login = input(Fore.CYAN + "Loginni kiriting:")
        password = input(Fore.CYAN + "Passwordni kiriting:")
        if login == "Jamshidbek" and password == "11.06.2004":
            for key, value in database.items():
                print("\n\n",key)
                for i in range(len(value[0])):
                    print(f"{value[0][i]} ==> {value[1][i]}", end="  ")
        else:
            print(Fore.LIGHTRED_EX + "Siz uchun bu bo'limga ruxsat yo'q!")

    elif bolim == "0":
        break




