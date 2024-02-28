# from colorama import init, Fore, Back
# init(autoreset=True)
from datetime import datetime, timedelta

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
database1 = {}
database2 = {}
database3 = {}
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
                    # print(add_database_key)
                    if not(bool(select_name_list)):
                        for key, value in database[add_database_key].items():
                            select_name_list.append(key)

                    for i in range(len(select_name_list)):
                        print(i + 1, select_name_list[i])
                    add_database_value_key = input("Mahsulotni nomini nomerini kiriting/Jadvalda mavjud bo'lmasa nomini aniq kiriting(kamida 5 ta harfli so'z bo'lsin:):")

                    while True:
                        date_year = input("Yaroqlilik yili:")
                        if date_year.isdigit():
                            date_year = int(date_year)
                            break
                        else:
                            print("Yilni kiritishda xatolikka yo'l qo'ydingiz!Iltimos,boshqatdan urinib ko'ring!:")
                    if date_year < 2024:
                        print("Ushbu mahsulotning muddati o'tgan!Kechirasiz bazaga qo'sha olmaymiz!")
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
                        add_database_value_value_value1 = input(select_sort_list[0])                                     # Miqdori
                        if add_database_value_value_value1.isdigit() and int(add_database_value_value_value1) > 0:
                            add_database_value_value_value1 = int(add_database_value_value_value1)
                            break
                        else:
                            print("Miqdori kiritishda xatolikka yo'l qo'ydingiz!Iltimos boshqatdan urininib ko'ring!")
                    add_database_value_value_value3 = datetime.now()                                                   # Kelgan sanasi
                    add_database_value_value_value4 = datetime(date_year, date_moth, date_day)                           # Yaroqlilik muddati

                    add_database_value_value_value5 = input(select_sort_list[4])                                       # Mamlakati


                    if add_database_value_key.isdigit() and int(add_database_value_key) < len(select_name_list):        # Qo'shiladigan mahsulot menyuda bor
                        add_database_value_key = select_name_list[int(add_database_value_key) - 1]
                        add_database_value_value_value2 = database[add_database_key][add_database_value_key][select_sort_list[1]]    # Narxi
                        
                        database[add_database_key][add_database_value_key][select_sort_list[0]] += add_database_value_value_value1      # DATABASE GA Miqdor qo'shish
                        database[add_database_key][add_database_value_key][select_sort_list[2]] = add_database_value_value_value3       # DATABASEGA Kelgan sanani update qilish
                        database[add_database_key][add_database_value_key][select_sort_list[3]] = add_database_value_value_value4       # DATABASEGA Srogini update qilish













                    else:                                                                                               #Qo'shiladigan mahsulot menyuda bo'lmasa
                        select_name_list.append(add_database_value_key)
                        while True:
                            add_database_value_value_value2 = input(select_sort_list[1])
                            if add_database_value_value_value2.isdigit() and int(add_database_value_value_value2) > 0:
                                add_database_value_value_value2 = int(add_database_value_value_value2)
                                break
                            else:
                                print("Narxini xato kiritdingiz!Qayta kiriting!")

























                elif int(add_database_key) == 0:
                    break

                else:
                    print("MAHSULOT TURKUMINI XATO KIRITDINGIZ!ILTIMOS BOSHQATDAN KIRITING:")

        # ___________________________________________________________SELL BOLIMI__________________________________________________________________________
        elif select_page == 2:
            while True:
                pass
            pass

        # ______________________________________________________________REPORT__________________________________________________________________________
        elif select_page == 3:
            while True:
                pass
            pass
        # ______________________________________________________DATABASENI KO'RISH BOLIMI__________________________________________________________________________
        elif select_page == 4:
            pass
    else:
        print("SAHIFANI NOMERINI XATO KIRITDINGIZ!ILTIMOS BOSHQATDAN TANLANG!")



# _________________________________________________________________FINISH PROGRAMM_______________________________________________________________________
print("DASTUR MUOFFAQQIYATLI YAKUNLANDI!".center(130))
print(database)