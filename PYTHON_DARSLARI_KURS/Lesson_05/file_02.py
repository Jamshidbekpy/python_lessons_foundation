from datetime import datetime

database = {
    "ICHIMLIKLAR": {
        "Cola": {
            "Miqdori:": 50,
            "Narxi:": 15000,
            "Kelgan sanasi:":datetime(2024, 11, 3),
            "Yaroqlilik muddati:": datetime(2026, 11, 3),
            "Ishlab chiqarilgan mamlakati": "Uzbekiston"
        },
        "Pepsi": {
            "Miqdori:": 50,
            "Narxi:": 13000,
            "Kelgan sanasi:": datetime(2024, 11, 12),
            "Yaroqlilik muddati:": datetime(2026, 11, 12),
            "Ishlab chiqarilgan mamlakati:": "Uzbekiston"
        },
    },
    "OZIQ-OVQAT": {
        "Non": {
            "Miqdori:": 50,
            "Narxi:": 1500,
            "Kelgan sanasi:": datetime(2024, 11, 7),
            "Yaroqlilik muddati:": datetime(2024, 11, 9),
            "Ishlab chiqarilgan mamlakati:": "Uzbekiston"
        },
        "Yog": {
            "Miqdori:": 50,
            "Narxi:": 20000,
            "Kelgan sanasi:": datetime(2024, 11, 5),
            "Yaroqlilik muddati:": datetime(2025, 11, 5),
            "Ishlab chiqarilgan mamlakati:": "Uzbekiston"
        },
    }
}
add_database = {
    "ICHIMLIKLAR": {
        "Cola": [

        ],
        "Pepsi": [

        ],
    },
    "OZIQ-OVQAT": {
        "Non": [

        ],
        "Yog": [

        ]
    }
}
add_database_value_dict = {}
sell_database = {
    "ICHIMLIKLAR": {
        "Cola": [

        ],
        "Pepsi": [

        ],
    },
    "OZIQ-OVQAT": {
        "Non": [

        ],
        "Yog": [

        ]
    }
}
sell_database_value_dict = {}
database1 = {}
database2 = {}
select_page_list = ["Add_product", "Sell_product", "Database", "Report"]
select_category_list = ["ICHIMLIKLAR", "OZIQ-OVQAT"]
select_name_list = []
select_sort_list = ["Miqdori:", "Narxi:", "Kelgan sanasi:", "Yaroqlilik muddati:", "Ishlab chiqarilgan mamlakati:"]

while True:
    for i in range(len(select_page_list)):
        print(i + 1, select_page_list[i])
#_____________________________________________________________SAHIFA TANLASH BO'LIMI____________________________________________________________________

    select_page = input("Yuqoridagi sahifalardan birini tanlang 1/2/3/4/0:").strip()
    if select_page.isdigit() and int(select_page) >= 0 and int(select_page) < 5:
        select_page = int(select_page)

        if select_page == 0:
            break
        # ___________________________________________________________ADD BOLIMI__________________________________________________________________________

        elif select_page == 1:
            while True:                                                                                                # TURKUMNI KIRITISH UCHUN
                print(0, "EXIT")
                for i in range(len(select_category_list)):
                    print(i + 1, select_category_list[i])                                                              # TURKUMLARNI CHOP ETISH

                add_database_key = input("MAHSULOT TURKUMINI KIRITING 1/2/0:")                                         # TURKUMLARNI TANLASH

                if add_database_key.isdigit() and int(add_database_key) > 0 and int(add_database_key) < 5:
                    add_database_key = select_category_list[int(add_database_key)-1]
                    print(add_database_key)
                    if not(bool(select_name_list)):
                        for key, value in database[add_database_key].items():
                            select_name_list.append(key)
                    print(0, "EXIT")
                    for i in range(len(select_name_list)):
                        print(i + 1, select_name_list[i])
                    while True:
                        add_database_value_key = input("Mahsulotni nomini nomerini kiriting/Jadvalda mavjud bo'lmasa nomini aniq kiriting(kamida 5 ta harfli so'z bo'lsin:)/0:")
                        if add_database_value_key == "0":
                            break
                        while True:
                            date_year = input("Yaroqlilik yili:")
                            if date_year.isdigit() and int(date_year) < 2040:
                                date_year = int(date_year)
                                break
                            else:
                                print("Yilni kiritishda xatolikka yo'l qo'ydingiz!Iltimos,boshqatdan urinib ko'ring!:")
                        if date_year < 2024:
                            print("Ushbu mahsulotning muddati o'tgan!Kechirasiz bazaga qo'sha olmaymiz!")
                            select_name_list.clear()
                            break
                        while True:
                            date_moth = input("Yaroqlilik oyi:")
                            if date_moth.isdigit() and int(date_moth) <= 12 and int(date_moth) > 0:
                                date_moth = int(date_moth)
                                break
                            else:
                                print("Oyni kiritishda xatolikka yo'l qo'ydingiz!Iltimos,boshqatdan urinib ko'ring!:")
                        while True:
                            date_day = input("Yaroqlilik kunini kiriting:")
                            if date_day.isdigit() and int(date_moth) > 0 and ((int(date_day) <= 31 and ((date_moth % 2 == 1 and date_moth <= 7) or (date_moth % 2 == 0 and date_moth > 7))) or (int(date_day) <= 30 and ((date_moth % 2 == 0 and date_moth <= 7 and date_moth != 2) or (date_moth % 2 == 1 and date_moth > 7))) or (date_year % 4 != 0 and int(date_day) <= 28 and date_moth == 2) or (date_year % 4 == 0 and int(date_day) <= 29 and date_moth == 2)):
                                date_day = int(date_day)
                                break
                            else:
                                print("Kunni kiritishda xatolikka yo'l qo'ydingiz!Iltimos,boshqatdan urinib ko'ring!:")

                        while True:
                            add_database_value_value_value1 = input(select_sort_list[0])                                                     # Miqdori
                            if add_database_value_value_value1.isdigit() and int(add_database_value_value_value1) > 0:
                                add_database_value_value_value1 = int(add_database_value_value_value1)
                                break
                            else:
                                print("Miqdori kiritishda xatolikka yo'l qo'ydingiz!Iltimos boshqatdan urininib ko'ring!")
                        add_database_value_value_value3 = datetime.now()                                                                    # Kelgan sanasi
                        add_database_value_value_value4 = datetime(date_year, date_moth, date_day)                                          # Yaroqlilik muddati

                        add_database_value_value_value5 = input(select_sort_list[4])                                                        # Mamlakati

                        if add_database_value_key.isdigit() and int(add_database_value_key) < len(select_name_list)+1 :                        # Qo'shiladigan mahsulot menyuda bor kola
                            add_database_value_key = select_name_list[int(add_database_value_key) - 1]
                            add_database_value_value_value2 = database[add_database_key][add_database_value_key][select_sort_list[1]]       # Narxi
                            database[add_database_key][add_database_value_key][select_sort_list[0]] += add_database_value_value_value1      # DATABASE GA Miqdor qo'shish
                            database[add_database_key][add_database_value_key][select_sort_list[2]] = add_database_value_value_value3       # DATABASEGA Kelgan sanani update qilish
                            database[add_database_key][add_database_value_key][select_sort_list[3]] = add_database_value_value_value4       # DATABASEGA Srogini update qilish
                            add_database_value_dict = add_database_value_dict.copy()
                            add_database_value_dict["Miqdori:"] = add_database_value_value_value1
                            add_database_value_dict["Narxi:"] = database[add_database_key][add_database_value_key]["Narxi:"]
                            add_database_value_dict["Jami narxi:"] = ((add_database_value_dict["Narxi:"])*add_database_value_value_value1)
                            add_database_value_dict["Kelgan sanasi:"] = add_database_value_value_value3
                            select_name_list.clear()

                        elif add_database_value_key in database[add_database_key]:
                            add_database_value_value_value2 = database[add_database_key][add_database_value_key][select_sort_list[1]]  # Narxi
                            database[add_database_key][add_database_value_key][select_sort_list[0]] += add_database_value_value_value1  # DATABASE GA Miqdor qo'shish
                            database[add_database_key][add_database_value_key][select_sort_list[2]] = add_database_value_value_value3  # DATABASEGA Kelgan sanani update qilish
                            database[add_database_key][add_database_value_key][select_sort_list[3]] = add_database_value_value_value4  # DATABASEGA Srogini update qilish
                            add_database_value_dict = add_database_value_dict.copy()
                            add_database_value_dict["Miqdori:"] = add_database_value_value_value1
                            add_database_value_dict["Narxi:"] = database[add_database_key][add_database_value_key]["Narxi:"]
                            add_database_value_dict["Jami narxi:"] = ((add_database_value_dict["Narxi:"]) * add_database_value_value_value1)
                            add_database_value_dict["Kelgan sanasi:"] = add_database_value_value_value3
                            select_name_list.clear()

                        else:                                                                                                               #Qo'shiladigan mahsulot menyuda bo'lmasa
                            select_name_list.append(add_database_value_key)
                            while True:
                                add_database_value_value_value2 = input(select_sort_list[1])
                                if add_database_value_value_value2.isdigit() and int(add_database_value_value_value2) > 0:
                                    add_database_value_value_value2 = int(add_database_value_value_value2)
                                    break
                                else:
                                    print("Narxini xato kiritdingiz!Qayta kiriting!")
                            database1[select_sort_list[0]] = add_database_value_value_value1
                            database1[select_sort_list[1]] = add_database_value_value_value2
                            database1[select_sort_list[2]] = add_database_value_value_value3
                            database1[select_sort_list[3]] = add_database_value_value_value4
                            database1[select_sort_list[4]] = add_database_value_value_value5
                            database2[add_database_value_key] = database1
                            database[add_database_key].setdefault(add_database_value_key, database1)
                            add_database_value_dict = add_database_value_dict.copy()
                            add_database[add_database_key].update({add_database_value_key: []})
                            add_database_value_dict["Miqdori:"] = add_database_value_value_value1
                            add_database_value_dict["Narxi:"] = database[add_database_key][add_database_value_key]["Narxi:"]
                            add_database_value_dict["Jami narxi:"] = ((add_database_value_dict["Narxi:"]) * add_database_value_value_value1)
                            add_database_value_dict["Kelgan sanasi:"] = add_database_value_value_value3
                            select_name_list.clear()
                        add_database[add_database_key][add_database_value_key].append(add_database_value_dict)
                elif int(add_database_key) == 0:
                    break
                else:
                    print("MAHSULOT TURKUMI NOMERINI XATO KIRITDINGIZ!ILTIMOS BOSHQATDAN KIRITING:")

        # ___________________________________________________________SELL BOLIMI__________________________________________________________________________
        elif select_page == 2:
            while True:
                print(0, "EXIT")
                for i in range(len(select_category_list)):
                    print(i + 1, select_category_list[i])                                                               # TURKUMLARNI CHOP ETISH

                sell_database_key = input("MAHSULOT TURKUMINI KIRITING 1/2/0:")                                         # TURKUMLARNI TANLASH

                if sell_database_key.isdigit() and int(sell_database_key) > 0 and int(sell_database_key) < 5:
                    sell_database_key = select_category_list[int(sell_database_key) - 1]
                    print(sell_database_key)
                    if not (bool(select_name_list)):
                        for key, value in database[sell_database_key].items():
                            select_name_list.append(key)
                    print(0, "Exit")
                    for i in range(len(select_name_list)):
                        print(i + 1, select_name_list[i])
                    while True:
                        sell_database_value_key = input("Mahsulotni nomini nomerini kiriting/Jadvaldan topolmasayiz aniq nomini kiriting!/0:")
                        if sell_database_value_key == "0":
                            select_name_list.clear()
                            break
                        elif sell_database_value_key in database[sell_database_key]:
                            sell_time = datetime.now()
                            while True:
                                sell_miqdor = input("Miqdorini kiriting:")
                                if sell_miqdor.isdigit():
                                    if database[sell_database_key][sell_database_value_key]["Miqdori:"] >= int(sell_miqdor):
                                        sell_miqdor = int(sell_miqdor)
                                        sell_database_value_dict = sell_database_value_dict.copy()
                                        sell_database_value_dict["Miqdori:"] = sell_miqdor
                                        sell_database_value_dict["Narxi:"] = (database[sell_database_key][sell_database_value_key]["Narxi:"]) / 100 * 115
                                        sell_database_value_dict["Jami narxi:"] = ((sell_database_value_dict["Narxi:"]) * float(sell_miqdor))
                                        sell_database_value_dict["Kelgan sanasi:"] = sell_time
                                        sell_database[sell_database_key][sell_database_value_key].append(sell_database_value_dict)
                                        database[sell_database_key][sell_database_value_key]["Miqdori:"] -= sell_miqdor
                                        print(f"Sotildi {sell_miqdor} miqdorda {sell_database_value_key} mahsuloti")
                                        select_name_list.clear()
                                        break
                                    elif sell_miqdor == "0":
                                        break
                                    else:
                                        print(
                                            f"Bizda ushbu mahsulotdan {database[sell_database_key][sell_database_value_key]['Miqdori:']} miqdorda qolgan!Olmoqchi bo'lsangiz kamroq hajm kiriting!Yo'qsa 0 ni kiriting!")
                                else:
                                    print("Iltimos midorga butun son kiriting!")

                        elif sell_database_value_key.isdigit() and len(select_name_list) >= int(sell_database_value_key):
                            sell_database_value_key = select_name_list[int(sell_database_value_key)-1]                  # Cola tanlash
                            select_name_list.clear()
                            sell_time = datetime.now()
                            while True:
                                sell_miqdor = input("Miqdorini kiriting:")
                                if sell_miqdor.isdigit():
                                    if database[sell_database_key][sell_database_value_key]["Miqdori:"] >= int(sell_miqdor):
                                        sell_miqdor = int(sell_miqdor)
                                        sell_database_value_dict = sell_database_value_dict.copy()
                                        sell_database_value_dict["Miqdori:"] = sell_miqdor
                                        sell_database_value_dict["Narxi:"] = (database[sell_database_key][sell_database_value_key]["Narxi:"])/100*115
                                        sell_database_value_dict["Jami narxi:"] = ((sell_database_value_dict["Narxi:"]) * float(sell_miqdor))
                                        sell_database_value_dict["Kelgan sanasi:"] = sell_time
                                        sell_database[sell_database_key][sell_database_value_key].append(sell_database_value_dict)
                                        database[sell_database_key][sell_database_value_key]["Miqdori:"] -= sell_miqdor
                                        print(f"Sotildi {sell_miqdor} miqdorda {sell_database_value_key} mahsuloti")
                                        break
                                    elif sell_miqdor == "0":
                                        break
                                    else:
                                        print(f"Bizda ushbu mahsulotdan {database[sell_database_key][sell_database_value_key]['Miqdori:']} miqdorda qolgan!Olmoqchi bo'lsangiz kamroq hajm kiriting!Yo'qsa 0 ni kiriting!")
                                else:
                                    print("Iltimos midorga butun son kiriting!")
                        else:
                            print("Mahsulot nomining nomerini xato kiritdingiz!Iltimos boshqatdan kiriting!")
                        break
                elif sell_database_key == "0":
                    break
                else:
                    print("MAHSULOT TURKUMI NOMERINI XATO KIRITDINGIZ!ILTIMOS BOSHQATDAN KIRITING:")

        # ____________________________________________________DATABASENI KO'RISH BOLIMI___________________________________________________________________
        elif select_page == 3:
            for key, value in database.items():
                print("\n\n", key.center(130))
                for key_01, value_01 in database[key].items():
                    print("\n", key_01)
                    for key_02,value_02 in database[key][key_01].items():
                        print(key_02, ":", value_02)
                    print(130*"_")
        # ______________________________________________________________REPORT__________________________________________________________________________
        elif select_page == 4:
            while True:
                n = 1
                add_sell = input("\nQo'shilgan mahsulotlar ro'yxati kerakmi yoki sotilgan +/-/0:")
                if add_sell == "0":
                    break
                elif add_sell == "+":
                    print("Kelgan mahsulotlar ro'yxati".center(130))
                    for k, v in add_database.items():
                        print(k.center(130))
                        for k_1, v_1 in add_database[k].items():
                            print(k_1, "\n-----------------------------------------")
                            for element in add_database[k][k_1]:
                                print("__________________________________________")
                                for k_2, v_2 in element.items():
                                    print(k_2, "==>", v_2)
                elif add_sell == "-":
                    print("Sotilgan ma'lumotlar ro'yxati:".center(130))
                    print(sell_database)
                    for k, v in sell_database.items():
                        print(k.center(130))
                        for k_1, v_1 in sell_database[k].items():
                            print(k_1, "\n-----------------------------------------")
                            for element in sell_database[k][k_1]:
                                print("__________________________________________")
                                for k_2, v_2 in element.items():
                                    print(k_2, "==>", v_2)
                else:
                    print("Bo'limni noto'g'ri tanladingiz!Chiqishni istasangiz 0 ni kiriting!")
    else:
        print("SAHIFANI NOMERINI XATO KIRITDINGIZ!ILTIMOS BOSHQATDAN TANLANG!")

# ___________________________________________________________________FINISH PROGRAMM_______________________________________________________________________
print("DASTUR MUOFFAQQIYATLI YAKUNLANDI!".center(130))